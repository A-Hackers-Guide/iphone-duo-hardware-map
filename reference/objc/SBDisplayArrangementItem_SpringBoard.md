# `SBDisplayArrangementItem`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreamable`
- 4 instance variables, 8 properties, 9 instance methods, 2 class methods

## Instance variables

```
I _edge;
@"FBSDisplayIdentity" _displayIdentity;
@"FBSDisplayIdentity" _relativeDisplayIdentity;
d _offset;
```

## Properties

```
@property (T@"FBSDisplayIdentity",R,N,V_displayIdentity) displayIdentity;
@property (T@"FBSDisplayIdentity",R,N,V_relativeDisplayIdentity) relativeDisplayIdentity;
@property (TI,R,N,V_edge) edge;
@property (Td,R,N,V_offset) offset;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBDisplayArrangementItem _preferredArrangementOfExternalDisplay:relativeToEmbeddedDisplay:preferences:];
+[SBDisplayArrangementItem preferredArrangementOfDisplay:relativeTo:preferences:];
```

## Instance methods

```
-[SBDisplayArrangementItem edge];
-[SBDisplayArrangementItem appendDescriptionToFormatter:];
-[SBDisplayArrangementItem hash];
-[SBDisplayArrangementItem description];
-[SBDisplayArrangementItem isEqual:];
-[SBDisplayArrangementItem displayIdentity];
-[SBDisplayArrangementItem offset];
-[SBDisplayArrangementItem relativeDisplayIdentity];
-[SBDisplayArrangementItem initWithDisplayIdentity:relativeDisplayIdentity:edge:offset:];
```
