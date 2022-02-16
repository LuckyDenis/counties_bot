CREATE TABLE "user" (
  "id" bigint UNIQUE PRIMARY KEY NOT NULL,
  "language" varchar(2) DEFAULT 'en',
  "game_name" varchar(36) UNIQUE,
  "is_admin" boolean NOT NULL DEFAULT false,
  "is_accept" boolean NOT NULL DEFAULT false,
  "is_block" boolean NOT NULL DEFAULT false,
  "registred" timestamp DEFAULT (now()),
  "visited" timestamp DEFAULT (now())
);

CREATE TABLE "wallet" (
  "user_id" bigint PRIMARY KEY NOT NULL,
  "gen_count" integer NOT NULL DEFAULT 0,
  "coin_count" integer NOT NULL DEFAULT 0
);

CREATE TABLE "game_item" (
  "id" integer PRIMARY KEY NOT NULL,
  "type" varchar(5) NOT NULL DEFAULT 'junk',
  "weight" float NOT NULL DEFAULT 0.001,
  "sell_price" integer DEFAULT 1,
  "sell_game_currency_id" varchar(4) NOT NULL DEFAULT 'coin'
);

CREATE TABLE "backpack" (
  "user_id" bigint NOT NULL,
  "backpack_cell" integer NOT NULL,
  "item_id" integer DEFAULT null,
  "item_count" integer DEFAULT 0,
  "is_select" boolean DEFAULT false,
  "is_used" boolean DEFAULT false,
  PRIMARY KEY ("user_id", "backpack_cell")
);

CREATE TABLE "recipe" (
  "id" integer UNIQUE NOT NULL,
  "product_id" integer UNIQUE NOT NULL,
  "product_count" integer NOT NULL DEFAULT 1,
  "work_price" integer NOT NULL DEFAULT 1,
  "work_price_game_currency_id" varchar(4) NOT NULL DEFAULT 'coin',
  PRIMARY KEY ("id", "product_id")
);

CREATE TABLE "store_product" (
  "id" integer UNIQUE PRIMARY KEY NOT NULL,
  "store_type_id" varchar(5) NOT NULL,
  "game_item_id" integer NOT NULL,
  "game_item_count" integer NOT NULL DEFAULT 1,
  "sell_price" integer NOT NULL DEFAULT 1,
  "sell_price_game_currency_id" varchar(4) NOT NULL DEFAULT 'coin'
);

CREATE TABLE "store_type" (
  "id" varchar(5) PRIMARY KEY NOT NULL
);

CREATE TABLE "recipe_component" (
  "recipe_id" integer NOT NULL,
  "game_item_id" integer NOT NULL,
  "game_item_count" integer NOT NULL DEFAULT 1,
  PRIMARY KEY ("recipe_id", "game_item_id")
);

CREATE TABLE "language" (
  "id" varchar(2) PRIMARY KEY NOT NULL
);

CREATE TABLE "game_item_type" (
  "id" varchar(5) PRIMARY KEY NOT NULL
);

CREATE TABLE "game_currency" (
  "id" varchar(4) PRIMARY KEY NOT NULL
);

ALTER TABLE "user" ADD FOREIGN KEY ("language") REFERENCES "language" ("id");

ALTER TABLE "wallet" ADD FOREIGN KEY ("user_id") REFERENCES "user" ("id");

ALTER TABLE "game_item" ADD FOREIGN KEY ("type") REFERENCES "game_item_type" ("id");

ALTER TABLE "game_item" ADD FOREIGN KEY ("sell_game_currency_id") REFERENCES "game_currency" ("id");

ALTER TABLE "backpack" ADD FOREIGN KEY ("user_id") REFERENCES "user" ("id");

ALTER TABLE "backpack" ADD FOREIGN KEY ("item_id") REFERENCES "game_item" ("id");

ALTER TABLE "recipe" ADD FOREIGN KEY ("product_id") REFERENCES "game_item" ("id");

ALTER TABLE "recipe" ADD FOREIGN KEY ("work_price_game_currency_id") REFERENCES "game_currency" ("id");

ALTER TABLE "store_product" ADD FOREIGN KEY ("store_type_id") REFERENCES "store_type" ("id");

ALTER TABLE "store_product" ADD FOREIGN KEY ("game_item_id") REFERENCES "game_item" ("id");

ALTER TABLE "store_product" ADD FOREIGN KEY ("sell_price_game_currency_id") REFERENCES "game_currency" ("id");

ALTER TABLE "recipe_component" ADD FOREIGN KEY ("game_item_id") REFERENCES "game_item" ("id");

CREATE INDEX "user_id__idx" ON "user" ("id");

CREATE INDEX "wallet_user_id__idx" ON "wallet" ("user_id");

CREATE INDEX "game_item_id__idx" ON "game_item" ("id");

CREATE INDEX "backpack_user_id__idx" ON "backpack" ("user_id");

CREATE INDEX "backpack_cell__idx" ON "backpack" ("user_id", "backpack_cell");

CREATE INDEX "recipe_id__idx" ON "recipe" USING HASH ("id");

CREATE INDEX "store_product_id__idx" ON "store_product" ("id");

CREATE INDEX "store_product__idx" ON "store_product" USING HASH ("store_type_id");

CREATE INDEX "store_type__idx" ON "store_type" ("id");

CREATE INDEX "recipe_component_recipe_id__idx" ON "recipe_component" ("recipe_id");

CREATE INDEX "recipe_component__idx" ON "recipe_component" ("recipe_id", "game_item_id");

CREATE INDEX "language_id__idx" ON "language" ("id");

CREATE INDEX "game_item_type_id__idx" ON "game_item_type" ("id");

CREATE INDEX "game_currency_id__idx" ON "game_currency" ("id");