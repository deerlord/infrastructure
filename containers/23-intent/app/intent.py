from adapt.engine import DomainIntentDeterminationEngine

engine = DomainIntentDeterminationEngine()



def handle_intent(instr):
    intent = engine.deterimine_intent(instr)


    return intent

intentions = engine.determine_intent(instr)


sleeping = os.path.isfile(EXECPATH + "/flags/sleeping")
for intent in intentions:
    if intent['keyword'] == 'help' and sleeping:
        execute_intent(intent, instr)
    elif intent['keyword'] == 'wake' and not sleeping:
        execute_intent(intent, instr)
        result = 1


    
