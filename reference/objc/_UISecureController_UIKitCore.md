# `_UISecureController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UISlotViewContentDelegate`
- 12 instance variables, 14 properties, 29 instance methods, 0 class methods

## Instance variables

```
@"UIControl<_UISecureControl>" _secureControl;
@"_UISlotView" _slotView;
@"_UISSecureControlSizeSpec" _lastSizeSpec;
B _shouldLayoutSynchronously;
B _enchanted;
q _cornerStyle;
d _cornerRadius;
^{CGColor=} _baseForegroundColor;
^{CGColor=} _baseBackgroundColor;
Q _imagePlacement;
@"_UISSecureControlCategory" _category;
{CGSize="width"d"height"d} _intrinsicContentSize;
```

## Properties

```
@property (Tq,N,V_cornerStyle) cornerStyle;
@property (Td,N,V_cornerRadius) cornerRadius;
@property (T^{CGColor=},N,V_baseForegroundColor) baseForegroundColor;
@property (T^{CGColor=},N,V_baseBackgroundColor) baseBackgroundColor;
@property (TQ,N,V_imagePlacement) imagePlacement;
@property (TB,N,V_shouldLayoutSynchronously) shouldLayoutSynchronously;
@property (T@"_UISSecureControlCategory",R,N,V_category) category;
@property (TB,R,N,V_enchanted) enchanted;
@property (T{CGSize=dd},R,N,V_intrinsicContentSize) intrinsicContentSize;
@property (TI,R,N) secureName;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UISecureController updateState];
-[_UISecureController cornerStyle];
-[_UISecureController intrinsicContentSize];
-[_UISecureController category];
-[_UISecureController setCornerStyle:];
-[_UISecureController dealloc];
-[_UISecureController setCornerRadius:];
-[_UISecureController secureName];
-[_UISecureController cornerRadius];
-[_UISecureController baseBackgroundColor];
-[_UISecureController baseForegroundColor];
-[_UISecureController currentTagForSlotView:];
-[_UISecureController enchanted];
-[_UISecureController imagePlacement];
-[_UISecureController initWithCategory:control:];
-[_UISecureController setBaseBackgroundColor:];
-[_UISecureController setBaseForegroundColor:];
-[_UISecureController setImagePlacement:];
-[_UISecureController setShouldLayoutSynchronously:];
-[_UISecureController shouldGetFinalContentSynchronouslyInSlotView:];
-[_UISecureController shouldLayoutSynchronously];
-[_UISecureController slotMachineForFinalContentInSlotView:];
-[_UISecureController slotView:didSetFinalContent:forStyle:tag:];
-[_UISecureController slotView:didSetInitialContent:forStyle:tag:];
-[_UISecureController slotView:initialContentForStyle:tag:];
-[_UISecureController slotView:replacementForFinalContent:style:tag:];
-[_UISecureController slotView:shouldSetFinalContentForStyle:tag:];
-[_UISecureController slotView:shouldSetInitialContentForStyle:tag:];
-[_UISecureController updateSlotView];
```
