FROM node:10.16.0-alpine

WORKDIR /app
COPY . .

RUN npm install
RUN npx tsc

EXPOSE 80

CMD ["node", "./dist/app.js"]