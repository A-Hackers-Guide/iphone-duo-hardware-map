# `_DUIImageComponent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 7 instance variables, 8 properties, 24 instance methods, 1 class methods

## Instance variables

```
{CAPoint3D="x"d"y"d"z"d} _origin;
{?="width"d"height"d"depth"d} _size;
B _ignoresAccessibilityFilters;
B _hidesImage;
I _slotID;
I _contextID;
Q _renderID;
```

## Properties

```
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N) frame;
@property (TB,N,V_ignoresAccessibilityFilters) ignoresAccessibilityFilters;
@property (TI,N,V_slotID) slotID;
@property (TQ,N,V_renderID) renderID;
@property (TI,N,V_contextID) contextID;
@property (T{?=ddd},N) size3D;
@property (TB,R,N) representsPortal;
@property (TB,N,V_hidesImage) hidesImage;
```

## Class methods

```
+[_DUIImageComponent supportsSecureCoding];
```

## Instance methods

```
-[_DUIImageComponent portalView];
-[_DUIImageComponent setContextID:];
-[_DUIImageComponent setHidesImage:];
-[_DUIImageComponent setSlotID:];
-[_DUIImageComponent imageComponent];
-[_DUIImageComponent encodeWithCoder:];
-[_DUIImageComponent slotID];
-[_DUIImageComponent setFrame:];
-[_DUIImageComponent hash];
-[_DUIImageComponent description];
-[_DUIImageComponent initWithCoder:];
-[_DUIImageComponent contextID];
-[_DUIImageComponent isEqual:];
-[_DUIImageComponent renderID];
-[_DUIImageComponent hidesImage];
-[_DUIImageComponent frame];
-[_DUIImageComponent setIgnoresAccessibilityFilters:];
-[_DUIImageComponent _configurePortalLayer:];
-[_DUIImageComponent createSnapshotViewForPreview:];
-[_DUIImageComponent ignoresAccessibilityFilters];
-[_DUIImageComponent representsPortal];
-[_DUIImageComponent setRenderID:];
-[_DUIImageComponent setSize3D:];
-[_DUIImageComponent size3D];
```
