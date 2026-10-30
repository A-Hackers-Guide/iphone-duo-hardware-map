# `SBSwitcherGenieAttributes`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 15 instance variables, 20 properties, 41 instance methods, 1 class methods

## Instance variables

```
B _active;
d _minimizedScale;
d _genieScale;
@"SBFFluidBehaviorSettings" _layoutSettings;
d _maximumGenieYAmount;
d _lateralAxisYLockThreshold;
{CGPoint="x"d"y"d} _iconPosition;
{CGPoint="x"d"y"d} _windowPosition;
{CGPoint="x"d"y"d} _initialVelocity;
{CGSize="width"d"height"d} _windowSize;
{CGSize="width"d"height"d} _minimizedSize;
{CGSize="width"d"height"d} _containerSize;
{CGSize="width"d"height"d} _minimumOutsetSize;
{CGPoint="x"d"y"d} _multiplier;
{SBSwitcherGenieGlassHighlight="style"Q"direction"{SBSwitcherGenieGlassHighlightDirection="x"d"y"d"z"d}"intensity"d} _glassHighlight;
```

## Properties

```
@property (TB,N,V_active) active;
@property (T{CGPoint=dd},N,V_iconPosition) iconPosition;
@property (T{CGPoint=dd},N,V_windowPosition) windowPosition;
@property (T{CGPoint=dd},N,V_initialVelocity) initialVelocity;
@property (T{CGSize=dd},N,V_windowSize) windowSize;
@property (T{CGSize=dd},N,V_minimizedSize) minimizedSize;
@property (Td,N,V_minimizedScale) minimizedScale;
@property (T{CGSize=dd},N,V_containerSize) containerSize;
@property (T{CGSize=dd},N,V_minimumOutsetSize) minimumOutsetSize;
@property (Td,N,V_genieScale) genieScale;
@property (T{CGPoint=dd},N,V_multiplier) multiplier;
@property (T{SBSwitcherGenieGlassHighlight=Q{SBSwitcherGenieGlassHighlightDirection=ddd}d},N,V_glassHighlight) glassHighlight;
@property (T@"SBFFluidBehaviorSettings",&,N,V_layoutSettings) layoutSettings;
@property (Td,N,V_maximumGenieYAmount) maximumGenieYAmount;
@property (Td,N,V_lateralAxisYLockThreshold) lateralAxisYLockThreshold;
@property (Tq,R,N) rows;
@property (Tq,R,N) columns;
@property (Tq,R,N) vertexCount;
@property (T{CGPoint=dd},R,N) genieAmount;
@property (Td,R,N) scaleProgress;
```

## Class methods

```
+[SBSwitcherGenieAttributes genieAttributesForIconPosition:windowPosition:initialVelocity:windowSize:minimizedSize:minimizedScale:containerSize:minimumOutsetSize:genieScale:multiplier:active:glassHighlight:layoutSettings:];
```

## Instance methods

```
-[SBSwitcherGenieAttributes columns];
-[SBSwitcherGenieAttributes containerSize];
-[SBSwitcherGenieAttributes genieAmount];
-[SBSwitcherGenieAttributes active];
-[SBSwitcherGenieAttributes setLateralAxisYLockThreshold:];
-[SBSwitcherGenieAttributes rows];
-[SBSwitcherGenieAttributes setInitialVelocity:];
-[SBSwitcherGenieAttributes setContainerSize:];
-[SBSwitcherGenieAttributes scaleProgress];
-[SBSwitcherGenieAttributes init];
-[SBSwitcherGenieAttributes meshContainerOutset];
-[SBSwitcherGenieAttributes windowSize];
-[SBSwitcherGenieAttributes setMultiplier:];
-[SBSwitcherGenieAttributes genieScale];
-[SBSwitcherGenieAttributes setMaximumGenieYAmount:];
-[SBSwitcherGenieAttributes multiplier];
-[SBSwitcherGenieAttributes minimizedProgress];
-[SBSwitcherGenieAttributes minimizedScale];
-[SBSwitcherGenieAttributes setActive:];
-[SBSwitcherGenieAttributes setMinimizedScale:];
-[SBSwitcherGenieAttributes vertexCount];
-[SBSwitcherGenieAttributes meshContainerSizeForSize:];
-[SBSwitcherGenieAttributes lateralAxisYLockThreshold];
-[SBSwitcherGenieAttributes setWindowSize:];
-[SBSwitcherGenieAttributes windowPosition];
-[SBSwitcherGenieAttributes minimizedSize];
-[SBSwitcherGenieAttributes glassHighlight];
-[SBSwitcherGenieAttributes initialVelocity];
-[SBSwitcherGenieAttributes setMinimumOutsetSize:];
-[SBSwitcherGenieAttributes counterOffsetForSize:];
-[SBSwitcherGenieAttributes maximumGenieYAmount];
-[SBSwitcherGenieAttributes setIconPosition:];
-[SBSwitcherGenieAttributes setWindowPosition:];
-[SBSwitcherGenieAttributes setLayoutSettings:];
-[SBSwitcherGenieAttributes setMinimizedSize:];
-[SBSwitcherGenieAttributes minimumOutsetSize];
-[SBSwitcherGenieAttributes setGenieScale:];
-[SBSwitcherGenieAttributes minimizedPositionForSize:];
-[SBSwitcherGenieAttributes layoutSettings];
-[SBSwitcherGenieAttributes iconPosition];
-[SBSwitcherGenieAttributes setGlassHighlight:];
```
