<script setup lang="ts">
import { computed, onMounted, ref } from 'vue';
import { pickOne, rectsOverlap, wait } from '../utils';

const model = defineModel<string>({ default: "" });

const props = withDefaults(defineProps<{
  refElem: HTMLElement
  /** Given as update interval, defaults to 1s */
  speed?: number
  /** Snake segment size (square), in px */
  snakeSize?: number
}>(), { speed: 750, snakeSize: 32 })

// In props.snakeSize
// const GRID_WIDTH = Math.ceil(props.refElem.clientWidth / props.snakeSize)
const GRID_HEIGHT = ref(Math.ceil(props.refElem.clientHeight / props.snakeSize))


type IndexedChars = Record<string, [Element, ChildNode, number][]>;
function indexText(chars: IndexedChars | null = null, element: Element = props.refElem): IndexedChars {
  if (chars === null) chars = Object.fromEntries(Array.from<unknown, [keyof IndexedChars, IndexedChars[string]]>({ length: 26 }, (_, i) => [String.fromCharCode("A".charCodeAt(0) + i), []]).concat(Array.from<unknown, [keyof IndexedChars, IndexedChars[string]]>({ length: 26 }, (_, i) => [String.fromCharCode("a".charCodeAt(0) + i), []])))

  for (const childNode of element.childNodes)
    if (childNode.nodeType === Node.TEXT_NODE)
      [...(childNode.textContent ?? "")].forEach((char, idx) => { if (char in chars) chars[char]!.push([element, childNode, idx]) })
  if (element.children) for (const childElem of element.children)
    indexText(chars, childElem)

  return chars
}

const apples: [string, HTMLSpanElement][] = []

function appleSpanIdFromChar(char: string) {
  return `snake-apple-${char}`
}
function makeAppleSpan(char: string) {
  return `<span id="${appleSpanIdFromChar(char)}" style="color: red;">${char}</span>`
}

function makeApplesForElement(element: Element, childNode: ChildNode, idxChars: [number, string][]) {
  idxChars.sort((a, b) => a[0] - b[0]);
  element.innerHTML = element.innerHTML.replace(childNode.textContent!, idxChars.reduce((acc, [idx, char], i, arr) => acc + makeAppleSpan(char) + childNode.textContent!.substring(idx + 1, i + 1 < arr.length ? arr[i + 1]![0] : undefined), childNode.textContent!.substring(0, idxChars[0]![0])))
  for (const [_, char] of idxChars) {
    const span = document.getElementById(appleSpanIdFromChar(char))
    if (span) apples.push([char, span])
  }
}

const initialSnakePartIdPrefix = "snake-init-"
type Coords = [number, number]
const initialSnakeCoords = computed<Coords[]>(() => [
  [3, Math.floor(GRID_HEIGHT.value / 2)],
  [2, Math.floor(GRID_HEIGHT.value / 2)],
  [1, Math.floor(GRID_HEIGHT.value / 2)],
])
const snake: [Coords, HTMLDivElement][] = [];
// An index of snake
let snakeHeadIdx: number = 0

const snakeClasses = ["absolute", "bg-green-400", "rounded-sm", "p-1", "bg-clip-content", "z-50"]

onMounted(async () => {
  await wait(1_000);

  GRID_HEIGHT.value = Math.ceil(props.refElem.clientHeight / props.snakeSize)

  // Get initial snake
  for (let i = 0; i < 3; ++i) {
    const snakePart = document.getElementById(`${initialSnakePartIdPrefix}${i}`)
    if (!snakePart) throw new Error(`Unexpected missing initial snake part`)

    snake.push([initialSnakeCoords.value[i]!, snakePart as HTMLDivElement])
  }

  const indexedChars = indexText()

  Array.from(Object.entries(indexedChars).reduce<Map<ChildNode, [Element, [number, string][]]>>((acc, [char, occurrences]) => {
    if (!occurrences.length) return acc;

    const [element, childNode, idx] = pickOne(occurrences)
    if (!acc.has(childNode)) acc.set(childNode, [element, []])
    acc.get(childNode)![1].push([idx, char])

    return acc;
  }, new Map()).entries()).forEach(([childNode, [element, idxs]]) => makeApplesForElement(element, childNode, idxs))
})

/**
 * Remove an apple and recreates a new one for the corresponding letter
 */
function eatApple(apple: (typeof apples)[number]) {
  // Remove apple in DOM: replace by corresponding letter
  apple[1].parentElement!.innerHTML = apple[1].parentElement!.innerHTML.replace(apple[1].outerHTML, apple[0])
  apples.splice(apples.indexOf(apple), 1)
  model.value += apple[0]

  // Add new apple for removed letter
  const indexedChars = indexText()
  const [newAppleElem, childNode, newAppleIdx] = pickOne(indexedChars[apple[0]]!)
  makeApplesForElement(newAppleElem, childNode, [[newAppleIdx, apple[0]]])
}


type Direction = [0, 0] | [0, 1] | [1, 0] | [0, -1] | [-1, 0]
let direction: Direction = [0, 0]

/**
 * O(|apples|)
 */
function findOverlappingApple(): (typeof apples)[number] | null {
  const snakeHeadRect = snake[snakeHeadIdx]![1].getBoundingClientRect();

  return apples.find(apple => rectsOverlap(snakeHeadRect, apple[1].getBoundingClientRect())) ?? null
}

document.addEventListener("keydown", (ev) => {
  switch (ev.code) {
    // Handle direction changes
    case "ArrowUp":
      direction = [0, -1]
      break;

    case "ArrowDown":
      direction = [0, 1]
      break;

    case "ArrowLeft":
      direction = [-1, 0]
      break;

    case "ArrowRight":
      direction = [1, 0]
      break;
  }
})

setInterval(async () => {
  if (direction.every(c => c == 0)) return;
  const prevTailIdx = snakeHeadIdx === 0 ? snake.length - 1 : snakeHeadIdx - 1
  const prevTailCoords = [...snake[prevTailIdx]![0]] as Coords
  snake[prevTailIdx]![0][0] = snake[snakeHeadIdx]![0][0] + direction[0]
  snake[prevTailIdx]![0][1] = snake[snakeHeadIdx]![0][1] + direction[1]
  snake[prevTailIdx]![1].style.left = `${snake[prevTailIdx]![0][0] * props.snakeSize}px`;
  snake[prevTailIdx]![1].style.top = `${snake[prevTailIdx]![0][1] * props.snakeSize}px`;

  snakeHeadIdx = prevTailIdx

  await wait(200)

  const overlappingApple = findOverlappingApple()
  if (overlappingApple !== null) {
    eatApple(overlappingApple)
    // Add snake part to tail
    const newSnakePartElem = document.createElement("div")
    newSnakePartElem.style.left = `${prevTailCoords[0] * props.snakeSize}px`
    newSnakePartElem.style.top = `${prevTailCoords[1] * props.snakeSize}px`
    newSnakePartElem.style.width = `${props.snakeSize}px`
    newSnakePartElem.style.height = `${props.snakeSize}px`
    snakeClasses.forEach(snakeClass => newSnakePartElem.classList.add(snakeClass))
    snake[0]![1].parentElement!.appendChild(newSnakePartElem)
    snake.splice(snakeHeadIdx === 0 ? snake.length - 1 : snakeHeadIdx - 1, 0, [prevTailCoords, newSnakePartElem])
    if (snakeHeadIdx > 0)
      // Correct snake head idx
      snakeHeadIdx++
  }
}, props.speed)
</script>

<template>
  <template v-for="([x, y], i) in initialSnakeCoords">
    <div :id="`${initialSnakePartIdPrefix}${i}`" :class="snakeClasses" :style="{
      left: `${x * snakeSize}px`,
      top: `${y * snakeSize}px`,
      width: `${snakeSize}px`,
      height: `${snakeSize}px`,
    }"></div>
  </template>
</template>