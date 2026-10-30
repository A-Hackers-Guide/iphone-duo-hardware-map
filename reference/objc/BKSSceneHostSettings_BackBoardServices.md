# `BKSSceneHostSettings`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreamable`, `NSSecureCoding`
- 2 instance variables, 6 properties, 10 instance methods, 2 class methods

## Instance variables

```
@"NSString" _identifier;
q _touchBehavior;
```

## Properties

```
@property (Tq,R,N,V_touchBehavior) touchBehavior;
@property (T@"NSString",R,N,V_identifier) identifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSSceneHostSettings supportsSecureCoding];
+[BKSSceneHostSettings new];
```

## Instance methods

```
-[BKSSceneHostSettings identifier];
-[BKSSceneHostSettings initWithIdentifier:touchBehavior:];
-[BKSSceneHostSettings init];
-[BKSSceneHostSettings appendDescriptionToFormatter:];
-[BKSSceneHostSettings touchBehavior];
-[BKSSceneHostSettings encodeWithCoder:];
-[BKSSceneHostSettings hash];
-[BKSSceneHostSettings description];
-[BKSSceneHostSettings initWithCoder:];
-[BKSSceneHostSettings isEqual:];
```
