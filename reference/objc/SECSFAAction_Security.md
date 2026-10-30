# `SECSFAAction`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 6 instance variables, 10 properties, 28 instance methods, 0 class methods

## Instance variables

```
@"SECSFAActionAutomaticBugCapture" _abc;
i _action;
@"SECSFAActionDropEvent" _drop;
@"NSString" _radarnumber;
@"SECSFAActionTapToRadar" _ttr;
{?="action"b1} _has;
```

## Properties

```
@property (TB,R,N) hasRadarnumber;
@property (T@"NSString",&,N,V_radarnumber) radarnumber;
@property (TB,R,N) hasTtr;
@property (T@"SECSFAActionTapToRadar",&,N,V_ttr) ttr;
@property (TB,R,N) hasAbc;
@property (T@"SECSFAActionAutomaticBugCapture",&,N,V_abc) abc;
@property (TB,R,N) hasDrop;
@property (T@"SECSFAActionDropEvent",&,N,V_drop) drop;
@property (TB,N) hasAction;
@property (Ti,N,V_action) action;
```

## Instance methods

```
-[SECSFAAction writeTo:];
-[SECSFAAction mergeFrom:];
-[SECSFAAction setAction:];
-[SECSFAAction action];
-[SECSFAAction drop];
-[SECSFAAction hash];
-[SECSFAAction copyTo:];
-[SECSFAAction description];
-[SECSFAAction readFrom:];
-[SECSFAAction copyWithZone:];
-[SECSFAAction isEqual:];
-[SECSFAAction dictionaryRepresentation];
-[SECSFAAction hasAction];
-[SECSFAAction setHasAction:];
-[SECSFAAction hasDrop];
-[SECSFAAction setAbc:];
-[SECSFAAction setRadarnumber:];
-[SECSFAAction StringAsAction:];
-[SECSFAAction abc];
-[SECSFAAction actionAsString:];
-[SECSFAAction setTtr:];
-[SECSFAAction ttr];
-[SECSFAAction clearOneofValuesForAction];
-[SECSFAAction hasAbc];
-[SECSFAAction hasRadarnumber];
-[SECSFAAction hasTtr];
-[SECSFAAction radarnumber];
-[SECSFAAction setDrop:];
```
