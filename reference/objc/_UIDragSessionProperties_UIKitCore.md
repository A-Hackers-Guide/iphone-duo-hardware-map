# `_UIDragSessionProperties`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 17 instance methods, 0 class methods

## Instance variables

```
B _supportsSystemDrag;
B __rotatable;
B __resizable;
B __wantsElasticEffects;
B __confineToLocalDevice;
B __avoidsKeyboardSuppression;
{CGSize="width"d"height"d} __minimumResizableSize;
{CGSize="width"d"height"d} __maximumResizableSize;
```

## Properties

```
@property (TB,N,V__avoidsKeyboardSuppression) _avoidsKeyboardSuppression;
@property (TB,N,V__rotatable) _rotatable;
@property (TB,N,V__resizable) _resizable;
@property (T{CGSize=dd},N,V__minimumResizableSize) _minimumResizableSize;
@property (T{CGSize=dd},N,V__maximumResizableSize) _maximumResizableSize;
@property (TB,N,V__wantsElasticEffects) _wantsElasticEffects;
@property (TB,N,V_supportsSystemDrag) _supportsSystemDrag;
@property (TB,N,V__confineToLocalDevice) _confineToLocalDevice;
```

## Instance methods

```
-[_UIDragSessionProperties init];
-[_UIDragSessionProperties _avoidsKeyboardSuppression];
-[_UIDragSessionProperties _confineToLocalDevice];
-[_UIDragSessionProperties _maximumResizableSize];
-[_UIDragSessionProperties _minimumResizableSize];
-[_UIDragSessionProperties _resizable];
-[_UIDragSessionProperties _rotatable];
-[_UIDragSessionProperties _supportsSystemDrag];
-[_UIDragSessionProperties _wantsElasticEffects];
-[_UIDragSessionProperties set_avoidsKeyboardSuppression:];
-[_UIDragSessionProperties set_confineToLocalDevice:];
-[_UIDragSessionProperties set_maximumResizableSize:];
-[_UIDragSessionProperties set_minimumResizableSize:];
-[_UIDragSessionProperties set_resizable:];
-[_UIDragSessionProperties set_rotatable:];
-[_UIDragSessionProperties set_supportsSystemDrag:];
-[_UIDragSessionProperties set_wantsElasticEffects:];
```
