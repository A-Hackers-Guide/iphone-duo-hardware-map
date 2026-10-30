# `_UISignalViewCacheKey`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 9 instance variables, 0 properties, 6 instance methods, 0 class methods

## Instance variables

```
# _classType;
{CGSize="width"d"height"d} _size;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _rect;
d _radius;
d _lineWidth;
{CGSize="width"d"height"d} _secondarySize;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _secondaryRect;
B _alternate;
d _scale;
```

## Instance methods

```
-[_UISignalViewCacheKey hash];
-[_UISignalViewCacheKey copyWithZone:];
-[_UISignalViewCacheKey isEqual:];
-[_UISignalViewCacheKey isEqualToCacheKey:];
-[_UISignalViewCacheKey initWithClass:size:rect:radius:lineWidth:alternate:scale:];
-[_UISignalViewCacheKey initWithClass:size:rect:radius:lineWidth:secondarySize:secondaryRect:alternate:scale:];
```
