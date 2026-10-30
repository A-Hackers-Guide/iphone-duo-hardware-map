# `SBButterflyPairResizeWindowingModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWindowingModifier`
- 25 instance variables, 0 properties, 31 instance methods, 0 class methods

## Instance variables

```
@"NSUUID" _gestureID;
@"SBDisplayItem" _leftDisplayItem;
@"SBDisplayItem" _rightDisplayItem;
@"SBAppLayout" _leftAppLayout;
@"SBAppLayout" _rightAppLayout;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _leftAppResizedFrame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _rightAppResizedFrame;
{CGPoint="x"d"y"d} _locationEdgeAdjustment;
d _initialGrabberMargin;
{CGPoint="x"d"y"d} _initialLocation;
d _translationThresholdForMaximizationOrMinimization;
d _screenScale;
B _gestureIsEnding;
@"SBDisplayItem" _itemToMinimizeUponRelease;
@"SBDisplayItem" _itemToMaximizeUponRelease;
@"SBAppLayout" _stretchingAppLayout;
@"SBAppLayout" _appLayoutPendingLiveContentRestore;
@"SBAppLayout" _blurredAppLayout;
@"SBAppLayout" _splitPairAppLayout;
B _prefersHomeAffordancesInItemContainers;
@"NSDictionary" _initialLayoutAttributesMap;
{SBWindowingItemFrame="bounds"{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}}"position"{CGPoint="x"d"y"d}"anchorPoint"{CGPoint="x"d"y"d}"scale"{CGPoint="x"d"y"d}"translation"{CGPoint="x"d"y"d}} _initialLeftItemFrame;
{SBWindowingItemFrame="bounds"{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}}"position"{CGPoint="x"d"y"d}"anchorPoint"{CGPoint="x"d"y"d}"scale"{CGPoint="x"d"y"d}"translation"{CGPoint="x"d"y"d}} _initialRightItemFrame;
q _initialHomeScreenVisibleScreenRegion;
q _currentHomeScreenVisibleScreenRegion;
```

## Instance methods

```
-[SBButterflyPairResizeWindowingModifier homeScreenScale];
-[SBButterflyPairResizeWindowingModifier isContainerStatusBarVisible];
-[SBButterflyPairResizeWindowingModifier homeScreenBackdropBlurProgress];
-[SBButterflyPairResizeWindowingModifier isHomeScreenContentRequired];
-[SBButterflyPairResizeWindowingModifier homeScreenBackdropBlurType];
-[SBButterflyPairResizeWindowingModifier init];
-[SBButterflyPairResizeWindowingModifier transitionWillBegin:];
-[SBButterflyPairResizeWindowingModifier wantsSceneResizesHostedContextForAppLayout:];
-[SBButterflyPairResizeWindowingModifier borderForItem:];
-[SBButterflyPairResizeWindowingModifier cornersForItem:];
-[SBButterflyPairResizeWindowingModifier frameForSplitViewHandleNubView:];
-[SBButterflyPairResizeWindowingModifier regionDividerCenter];
-[SBButterflyPairResizeWindowingModifier animationAttributesForItem:];
-[SBButterflyPairResizeWindowingModifier dimmingAlphaForItem:];
-[SBButterflyPairResizeWindowingModifier spaceAccessoryViewStrongPairIndicatorEdgeExtensionForAppLayout:];
-[SBButterflyPairResizeWindowingModifier isLayoutRoleMatchMovedToScene:inAppLayout:];
-[SBButterflyPairResizeWindowingModifier spaceAccessoryViewStrongPairIndicatorOpacityForAppLayout:];
-[SBButterflyPairResizeWindowingModifier frameForItem:];
-[SBButterflyPairResizeWindowingModifier hiddenContentStatusBarPartsForLayoutRole:inAppLayout:];
-[SBButterflyPairResizeWindowingModifier preferredSwitcherScreenRegionForAppLayout:];
-[SBButterflyPairResizeWindowingModifier willBegin];
-[SBButterflyPairResizeWindowingModifier didComplete];
-[SBButterflyPairResizeWindowingModifier _animationSettingsForLayout];
-[SBButterflyPairResizeWindowingModifier _blurParametersWithRadius:];
-[SBButterflyPairResizeWindowingModifier _displacementForItemToMinimizeUponRelease];
-[SBButterflyPairResizeWindowingModifier _shouldOverrideHomeScreenStyle];
-[SBButterflyPairResizeWindowingModifier _updateWithGesture:];
-[SBButterflyPairResizeWindowingModifier gestureDidComplete:];
-[SBButterflyPairResizeWindowingModifier gestureDidUpdate:];
-[SBButterflyPairResizeWindowingModifier gestureWillBegin:];
-[SBButterflyPairResizeWindowingModifier transitionDidComplete:];
```
