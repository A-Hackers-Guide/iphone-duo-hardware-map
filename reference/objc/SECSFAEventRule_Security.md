# `SECSFAEventRule`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 9 instance variables, 16 properties, 38 instance methods, 0 class methods

## Instance variables

```
q _repeatAfterSeconds;
@"SECSFAAction" _action;
i _eventClass;
@"NSString" _eventType;
@"NSData" _match;
@"NSString" _processName;
@"SECSFAVersionMatch" _versions;
B _matchOnFirstFailure;
{?="repeatAfterSeconds"b1"eventClass"b1"matchOnFirstFailure"b1} _has;
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
@property (TB,R,N) hasProcessName;
@property (T@"NSString",&,N,V_processName) processName;
@property (TB,N) hasEventClass;
@property (Ti,N,V_eventClass) eventClass;
@property (TB,R,N) hasVersions;
@property (T@"SECSFAVersionMatch",&,N,V_versions) versions;
@property (TB,N) hasMatchOnFirstFailure;
@property (TB,N,V_matchOnFirstFailure) matchOnFirstFailure;
```

## Instance methods

```
-[SECSFAEventRule setProcessName:];
-[SECSFAEventRule eventType];
-[SECSFAEventRule writeTo:];
-[SECSFAEventRule setEventType:];
-[SECSFAEventRule hasEventType];
-[SECSFAEventRule mergeFrom:];
-[SECSFAEventRule setAction:];
-[SECSFAEventRule action];
-[SECSFAEventRule eventClass];
-[SECSFAEventRule versions];
-[SECSFAEventRule processName];
-[SECSFAEventRule hash];
-[SECSFAEventRule copyTo:];
-[SECSFAEventRule description];
-[SECSFAEventRule readFrom:];
-[SECSFAEventRule copyWithZone:];
-[SECSFAEventRule isEqual:];
-[SECSFAEventRule hasProcessName];
-[SECSFAEventRule setVersions:];
-[SECSFAEventRule dictionaryRepresentation];
-[SECSFAEventRule hasAction];
-[SECSFAEventRule StringAsEventClass:];
-[SECSFAEventRule eventClassAsString:];
-[SECSFAEventRule hasEventClass];
-[SECSFAEventRule hasMatch];
-[SECSFAEventRule hasMatchOnFirstFailure];
-[SECSFAEventRule hasRepeatAfterSeconds];
-[SECSFAEventRule hasVersions];
-[SECSFAEventRule match];
-[SECSFAEventRule matchOnFirstFailure];
-[SECSFAEventRule repeatAfterSeconds];
-[SECSFAEventRule setEventClass:];
-[SECSFAEventRule setHasEventClass:];
-[SECSFAEventRule setHasMatchOnFirstFailure:];
-[SECSFAEventRule setHasRepeatAfterSeconds:];
-[SECSFAEventRule setMatch:];
-[SECSFAEventRule setMatchOnFirstFailure:];
-[SECSFAEventRule setRepeatAfterSeconds:];
```
