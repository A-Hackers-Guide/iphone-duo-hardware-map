# `_UITextCursorIntelligenceAnimation`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UITextCursorAnimation`
- 6 instance variables, 8 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"UIView" _glowView;
@"_UITextCursorIntelligenceGradientView" _gradientView;
B _enabled;
B _useCompactSize;
@"UIView" _cursorShapeView;
@"UIStandardTextCursorView" _cursorView;
```

## Properties

```
@property (T@"UIStandardTextCursorView",W,N,V_cursorView) cursorView;
@property (TB,N,V_useCompactSize) useCompactSize;
@property (T@"UIView",R,W,N,V_cursorShapeView) cursorShapeView;
@property (TB,N,GisEnabled,V_enabled) enabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UITextCursorIntelligenceAnimation setUseCompactSize:];
-[_UITextCursorIntelligenceAnimation cursorShapeDidChange];
-[_UITextCursorIntelligenceAnimation setCursorView:];
-[_UITextCursorIntelligenceAnimation isEnabled];
-[_UITextCursorIntelligenceAnimation _blurFilterWithRadius:];
-[_UITextCursorIntelligenceAnimation _setupGlowView];
-[_UITextCursorIntelligenceAnimation setEnabled:];
-[_UITextCursorIntelligenceAnimation _setupGradientView];
-[_UITextCursorIntelligenceAnimation initWithCursorShapeView:];
-[_UITextCursorIntelligenceAnimation cursorShapeView];
-[_UITextCursorIntelligenceAnimation useCompactSize];
-[_UITextCursorIntelligenceAnimation cursorView];
```
