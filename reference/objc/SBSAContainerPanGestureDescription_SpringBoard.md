# `SBSAContainerPanGestureDescription`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSAGestureDescription`
- 2 instance variables, 2 properties, 10 instance methods, 2 class methods

## Instance variables

```
{CGPoint="x"d"y"d} _initialLocation;
{CGPoint="x"d"y"d} _translation;
```

## Properties

```
@property (T{CGPoint=dd},N,S_setInitialLocation:,V_initialLocation) initialLocation;
@property (T{CGPoint=dd},N,S_setTranslation:,V_translation) translation;
```

## Class methods

```
+[SBSAContainerPanGestureDescription initialize];
+[SBSAContainerPanGestureDescription mutatorClass];
```

## Instance methods

```
-[SBSAContainerPanGestureDescription initialLocation];
-[SBSAContainerPanGestureDescription encodeWithCoder:];
-[SBSAContainerPanGestureDescription hash];
-[SBSAContainerPanGestureDescription description];
-[SBSAContainerPanGestureDescription copyWithZone:];
-[SBSAContainerPanGestureDescription isEqual:];
-[SBSAContainerPanGestureDescription translation];
-[SBSAContainerPanGestureDescription membersForCoder];
-[SBSAContainerPanGestureDescription _setInitialLocation:];
-[SBSAContainerPanGestureDescription _setTranslation:];
```
