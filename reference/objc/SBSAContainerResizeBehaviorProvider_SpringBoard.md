# `SBSAContainerResizeBehaviorProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSABasePreferencesProvider`
- 10 instance variables, 0 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _elementContexts;
{?="interfaceOrientation"q"layoutDirection"q"statusBarAxis"q"sensorVariant"Q} _orientationEnvironment;
@"SBSAContainerPanGestureDescription" _activeGestureDescription;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _initialFrameOfContainerViewForActiveGesture;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _initialContentFrameForActiveGesture;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _minimumFrameOfContainerViewForActiveGesture;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _lastResizedFrameForActiveGesture;
B _growthAxisIsVerticalForActiveGesture;
B _hasGrowthAxisForActiveGesture;
q _resizeGestureResult;
```

## Class methods

```
+[SBSAContainerResizeBehaviorProvider initialize];
```

## Instance methods

```
-[SBSAContainerResizeBehaviorProvider membersForCoder];
-[SBSAContainerResizeBehaviorProvider _collapseAxisIsVerticalWithGestureDescription:initialContainerViewFrame:layoutCollapseAxisIsVertical:context:];
-[SBSAContainerResizeBehaviorProvider _contentResizeBehaviorSettings];
-[SBSAContainerResizeBehaviorProvider _detachedCustomResizedFrameForContainerViewDescription:resizedWithGestureDescription:initialContainerViewFrame:geometry:context:];
-[SBSAContainerResizeBehaviorProvider _didGestureCollapseContainerFromFrame:toFrame:geometry:translation:role:context:];
-[SBSAContainerResizeBehaviorProvider _frameForAdjunctContainerViewDescription:resizedWithGestureDescription:initialContainerViewFrame:context:];
-[SBSAContainerResizeBehaviorProvider _frameForContainerViewDescription:resizedWithGestureDescription:initialContainerViewFrame:geometry:context:];
-[SBSAContainerResizeBehaviorProvider _preferencesUpdatedWithCollapseOfElement:activeFrame:initialFrame:minimumFrame:collapseAxisIsVertical:preferences:context:];
-[SBSAContainerResizeBehaviorProvider preferencesFromContext:];
```
