BEGIN;
--
-- Create model Question
--
CREATE TABLE "polls_question" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "question_text" varchar(200) NOT NULL, "pub_date" datetime NOT NULL);
--
-- Create model Choice
--
CREATE TABLE "polls_choice" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "choice_text" varchar(200) NOT NULL, "votes" integer NOT NULL, "question_id" bigint NOT NULL REFERENCES "polls_question" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "polls_choice_question_id_c5b4b260" ON "polls_choice" ("question_id");
COMMIT;



BEGIN;
--
-- Add field facilitator to question
--
CREATE TABLE "new__polls_question" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "facilitator" varchar(200) NOT NULL, "question_text" varchar(200) NOT NULL, "pub_date" datetime NOT NULL);
INSERT INTO "new__polls_question" ("id", "question_text", "pub_date", "facilitator") SELECT "id", "question_text", "pub_date", 'Facilitator 1' FROM "polls_question";
DROP TABLE "polls_question";
ALTER TABLE "new__polls_question" RENAME TO "polls_question";
COMMIT;