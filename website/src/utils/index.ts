function pickOne<T>(arr: T[]): T {
  return arr[Math.floor(Math.random() * arr.length)]!;
}

function rectsOverlap(rect1: DOMRect, rect2: DOMRect) {
  return !(
    rect1.right < rect2.left ||
    rect1.left > rect2.right ||
    rect1.bottom < rect2.top ||
    rect1.top > rect2.bottom
  );
}

type resolveCb<T = void> = (value: T) => void;
// eslint-disable-next-line @typescript-eslint/no-explicit-any
type rejectCb = (reason?: any) => void;
class Deferred<T = unknown> {
  public promise: Promise<T>;
  public resolve!: resolveCb<T>;
  public reject!: rejectCb;

  constructor() {
    this.promise = new Promise<T>((resolve, reject) => {
      this.reject = reject;
      this.resolve = resolve;
    });
  }
}

/**
 * Asynchronously pause code
 * @param ms Time to wait, defaults to 1s
 * @returns Promise to await
 * @example await wait(1_000) // Pause code execution for 1s
 */
function wait(ms = 1000): Promise<void> {
  const defP = new Deferred<void>();

  setTimeout(() => {
    defP.resolve();
  }, ms);

  return defP.promise;
}

export { pickOne, rectsOverlap, wait };
