IS_USER_EXIST = """
SELECT EXISTS(
    SELECT "id"
    FROM "public"."user"
    WHERE "id" = $1
);
"""

CREATE_NEW_USER = """
INSERT INTO "public"."user" (id, language)
VALUES($1, $2);
"""


IS_USER_ACCEPT = """
SELECT EXISTS(
    SELECT "id"
    FROM "public"."user"
    WHERE "id" = $1
    AND "is_accept" = true
);
"""


GET_USER_LANGUAGE = """
SELECT "language"
FROM "public"."user"
WHERE "id" = $1;
"""


UPDATE_USER_ACCEPT = """
UPDATE "public"."user"
SET "is_accept" = $2
WHERE "id" = $1;
"""
