# `SECSFARule`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 7 instance variables, 12 properties, 31 instance methods, 0 class methods

## Instance variables

```
q _repeatAfterSeconds;
@"SECSFAAction" _action;
i _eventClass;
@"NSString" _eventType;
@"NSData" _match;
@"NSString" _process;
{?="repeatAfterSeconds"b1"eventClass"b1} _has;
```

## Properties

```
@property (TB,R,N) hasEventType;
@property (T@"NSString",&,N,V_eventType) eventType;
@property (TB,R,N) hasMatch;
@property (T@"NSData",&,N,V_match) match;
@property (TB,R,N) hasAction;
@property (T@"SECSFAAction",&,N,V_action) action;
@property (TB,N) hasRepeatAfterSeconds;
@property (Tq,N,V_repeatAfterSeconds) repeatAfterSeconds;
@property (TB,R,N) hasProcess;
@property (T@"NSString",&,N,V_process) process;
@property (TB,N) hasEventClass;
@property (Ti,N,V_eventClass) eventClass;
```

## Instance methods

```
-[SECSFARule eventType];
-[SECSFARule writeTo:];
-[SECSFARule setProcess:];
-[SECSFARule setEventType:];
-[SECSFARule hasEventType];
-[SECSFARule mergeFrom:];
-[SECSFARule process];
-[SECSFARule setAction:];
-[SECSFARule action];
-[SECSFARule eventClass];
-[SECSFARule hash];
-[SECSFARule copyTo:];
-[SECSFARule description];
-[SECSFARule readFrom:];
-[SECSFARule copyWithZone:];
-[SECSFARule isEqual:];
-[SECSFARule dictionaryRepresentation];
-[SECSFARule hasAction];
-[SECSFARule StringAsEventClass:];
-[SECSFARule eventClassAsString:];
-[SECSFARule hasEventClass];
-[SECSFARule hasMatch];
-[SECSFARule hasProcess];
-[SECSFARule hasRepeatAfterSeconds];
-[SECSFARule match];
-[SECSFARule repeatAfterSeconds];
-[SECSFARule setEventClass:];
-[SECSFARule setHasEventClass:];
-[SECSFARule setHasRepeatAfterSeconds:];
-[SECSFARule setMatch:];
-[SECSFARule setRepeatAfterSeconds:];
```
