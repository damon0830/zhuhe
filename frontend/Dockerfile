# ============================================================
# 珠合 (ZhuHe) — 前端生产 Dockerfile
# Nuxt 3 SSR 多阶段构建
# ============================================================

# -------- 构建阶段 ----------
FROM node:20-alpine AS builder

WORKDIR /app

# 1. 仅复制依赖文件，利用 Docker 缓存层
COPY package.json ./
RUN npm install

# 2. 复制源码并构建
COPY . .
RUN npm run build

# -------- 运行阶段 ----------
FROM node:20-alpine AS runner

WORKDIR /app

# 安装 tini 用于优雅处理信号
RUN apk add --no-cache tini

# 从构建阶段复制产物
COPY --from=builder /app/.output /app/.output
COPY --from=builder /app/node_modules /app/node_modules
COPY --from=builder /app/package.json /app/package.json

EXPOSE 3000

ENV NUXT_HOST=0.0.0.0
ENV NUXT_PORT=3000
ENV NUXT_PUBLIC_API_BASE=/api

# 使用 tini 确保信号正确处理
ENTRYPOINT ["/sbin/tini", "--"]
CMD ["node", ".output/server/index.mjs"]
