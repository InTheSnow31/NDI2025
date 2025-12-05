/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly VITE_AUDIOVIZ_BACKEND_URL: string;
}

interface ImportMeta {
  readonly env: ImportMetaEnv;
}
