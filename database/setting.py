from . import DB, get_stuff

AL = DB.get("YESCAPTION")
if not AL:
    DB.set("YESCAPTION", "{'USERS':[]}")

ML = DB.get("NOCAPTION")
if not ML:
    DB.set("NOCAPTION", "{'USERS':[]}")


def caption_True(id):
    CA = get_stuff("YESCAPTION")
    CN = get_stuff("NOCAPTION")
    if CN and CN["USERS"]:
      USR = CN["USERS"]
      if id in USR:
        USR.remove(id)
        CN.update({"USERS":USR})
        DB.set("NOCAPTION", str(CN))
    LT = {"USERS":[id]}
    if CA:
        if not CA["USERS"]:
          DB.set("YESCAPTION", str(LT))
          return True
        if id not in CA["USERS"]:
          lm = CA["USERS"]
          lm.append(id)
          CA.update({"USERS":lm})
          DB.set("YESCAPTION", str(CA))
          return True
    else:
      DB.set("YESCAPTION", str(LT))
      return True


def caption_False(id):
    CA = get_stuff("NOCAPTION")
    CN = get_stuff("YESCAPTION")
    if CN and CN["USERS"]:
      USR = CN["USERS"]
      if id in USR:
        USR.remove(id)
        CN.update({"USERS":USR})
        DB.set("YESCAPTION", str(CN))
    LT = {"USERS":[id]}
    if CA:
        if not CA["USERS"]:
          DB.set("NOCAPTION", str(LT))
          return True
        if id not in CA["USERS"]:
          lm = CA["USERS"]
          lm.append(id)
          CA.update({"USERS":lm})
          DB.set("NOCAPTION", str(CA))
          return True
    else:
      DB.set("NOCAPTION", str(LT))
      return True


def check_settings(id):
    CA = get_stuff("YESCAPTION")
    CN = get_stuff("NOCAPTION")
    if not (CN or CA):
        return "None"
    if CA and CA["USERS"] and id in CA["USERS"]:
        return "True"
    if CN and CN["USERS"] and id in CN["USERS"]:
        return "False"
