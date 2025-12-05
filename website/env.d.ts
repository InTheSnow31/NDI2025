/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly AUDIOVIZ_BACKEND_URL: string;
}

interface ImportMeta {
  readonly env: ImportMetaEnv;
}
