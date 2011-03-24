from django.db import connection, transaction
import settings

import re
from django.db import connection, transaction
from django.db.models import Q
from forum.models.question import Question, QuestionManager
from forum.models.node import Node
from forum.modules import decorate

if not bool(settings.MYSQL_FTS_INDEXES_INSTALLED):
    try:
        cursor = connection.cursor()
        cursor.execute("ALTER TABLE forum_node ADD FULLTEXT(title, body, tagnames);")
        transaction.commit_unless_managed()

        settings.MYSQL_FTS_INDEXES_INSTALLED.set_value(True)

    except Exception, e:
        #import sys, traceback
        #traceback.print_exc(file=sys.stdout)
        pass
    finally:
        cursor.close()

word_re = re.compile(r'\w+', re.UNICODE)

@decorate(QuestionManager.search, needs_origin=False)
def question_search(self, keywords):
    q = "".join(["+%s " % w for w in word_re.findall(keywords)])

    return False, self.extra(
            where=["MATCH(title, body, tagnames) AGAINST(%s IN BOOLEAN MODE)"],
            params=[q],
            )