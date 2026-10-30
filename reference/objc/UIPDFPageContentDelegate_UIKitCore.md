# `UIPDFPageContentDelegate`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CALayerDelegate`
- 13 instance variables, 13 properties, 25 instance methods, 0 class methods

## Instance variables

```
@"UIPDFDocument" _document;
Q _pageIndex;
@"UIPDFPageView" _view;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _bounds;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _transform;
^{CGColor=} _white;
^{CGColor=} _highlightColor;
@"CALayer" _owner;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _box;
Q _pageRotation;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
Q _threadCount;
B _isCancelled;
```

## Properties

```
@property (T@"UIPDFDocument",&,V_document) document;
@property (TQ,V_pageIndex) pageIndex;
@property (T@"UIPDFPageView",D) view;
@property (T@"CALayer",V_owner) owner;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},V_box) box;
@property (TQ,V_pageRotation) pageRotation;
@property (T^{CGColor=},V_highlightColor) highlightColor;
@property (T{CGAffineTransform=dddddd},R,V_transform) transform;
@property (TB,D) isCancelled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIPDFPageContentDelegate owner];
-[UIPDFPageContentDelegate document];
-[UIPDFPageContentDelegate setPageIndex:];
-[UIPDFPageContentDelegate init];
-[UIPDFPageContentDelegate dealloc];
-[UIPDFPageContentDelegate drawLayer:inContext:];
-[UIPDFPageContentDelegate isCancelled];
-[UIPDFPageContentDelegate setView:];
-[UIPDFPageContentDelegate setOwner:];
-[UIPDFPageContentDelegate setHighlightColor:];
-[UIPDFPageContentDelegate transform];
-[UIPDFPageContentDelegate setDocument:];
-[UIPDFPageContentDelegate view];
-[UIPDFPageContentDelegate pageIndex];
-[UIPDFPageContentDelegate highlightColor];
-[UIPDFPageContentDelegate box];
-[UIPDFPageContentDelegate setBox:];
-[UIPDFPageContentDelegate setIsCancelled:];
-[UIPDFPageContentDelegate addRect:toPath:transform:view:owner:];
-[UIPDFPageContentDelegate computeTransform];
-[UIPDFPageContentDelegate drawSelectionLayer:inContext:];
-[UIPDFPageContentDelegate drawSelectionLayerBlockMode:inContext:];
-[UIPDFPageContentDelegate pageHasSelection];
-[UIPDFPageContentDelegate pageRotation];
-[UIPDFPageContentDelegate setPageRotation:];
```
