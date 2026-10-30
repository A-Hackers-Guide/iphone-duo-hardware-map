# `_SBDisplayItemFlexibleGrid`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_SBDisplayItemGridProvider`
- 5 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"SBSwitcherWindowingSettings" _settings;
@"SBSwitcherWindowingConfiguration" _windowingConfiguration;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _bounds;
@"NSArray" _widths;
@"NSArray" _heights;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_SBDisplayItemFlexibleGrid minSize];
-[_SBDisplayItemFlexibleGrid maxSize];
-[_SBDisplayItemFlexibleGrid _buildGridWithScreenScale:];
-[_SBDisplayItemFlexibleGrid _gridHeightsForSafeHeight:minimumHeight:];
-[_SBDisplayItemFlexibleGrid _gridWidthsForSafeWidth:minimumWidth:];
-[_SBDisplayItemFlexibleGrid allHeights];
-[_SBDisplayItemFlexibleGrid allWidths];
-[_SBDisplayItemFlexibleGrid initWithBounds:screenScale:windowingConfiguration:];
-[_SBDisplayItemFlexibleGrid nearestGridSizeForSize:countOnStage:];
-[_SBDisplayItemFlexibleGrid sizeAtIndexFromFullWidthForBounds:];
```
