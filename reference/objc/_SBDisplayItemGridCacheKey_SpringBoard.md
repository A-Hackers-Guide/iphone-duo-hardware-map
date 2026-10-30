# `_SBDisplayItemGridCacheKey`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 6 instance variables, 0 properties, 4 instance methods, 0 class methods

## Instance variables

```
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _bounds;
q _orientation;
@"SBDisplayItemGridLayoutRestrictionInfo" _layoutRestrictionInfo;
d _screenScale;
@"SBSwitcherWindowingConfiguration" _windowingConfiguration;
Q _cachedHash;
```

## Instance methods

```
-[_SBDisplayItemGridCacheKey hash];
-[_SBDisplayItemGridCacheKey copyWithZone:];
-[_SBDisplayItemGridCacheKey isEqual:];
-[_SBDisplayItemGridCacheKey initWithBounds:orientation:layoutRestrictionInfo:screenScale:windowingConfiguration:];
```
