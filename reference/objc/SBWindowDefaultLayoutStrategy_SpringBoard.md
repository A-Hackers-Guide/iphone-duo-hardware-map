# `SBWindowDefaultLayoutStrategy`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBWindowLayoutStrategy`
- 1 instance variables, 4 properties, 5 instance methods, 3 class methods

## Instance variables

```
B _clip;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBWindowDefaultLayoutStrategy _strategyWithClipping:];
+[SBWindowDefaultLayoutStrategy clipStrategy];
+[SBWindowDefaultLayoutStrategy noClipStrategy];
```

## Instance methods

```
-[SBWindowDefaultLayoutStrategy removeObserver:];
-[SBWindowDefaultLayoutStrategy _init];
-[SBWindowDefaultLayoutStrategy addObserver:];
-[SBWindowDefaultLayoutStrategy frameWithInterfaceOrientation:windowScene:];
-[SBWindowDefaultLayoutStrategy shouldClipForWindow:];
```
