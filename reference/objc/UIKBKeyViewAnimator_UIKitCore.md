# `UIKBKeyViewAnimator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAAnimationDelegate`
- 2 instance variables, 9 properties, 38 instance methods, 4 class methods

## Instance variables

```
B _disabled;
d _keyScale;
```

## Properties

```
@property (Td,N,V_keyScale) keyScale;
@property (TB,N,V_disabled) disabled;
@property (TB,R,N) shouldPurgeKeyViews;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) primaryGlyphNormalizedExitRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) secondaryGlyphNormalizedExitRect;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIKBKeyViewAnimator normalizedAnimationWithKeyPath:fromValue:toValue:];
+[UIKBKeyViewAnimator normalizedUnwindAnimationWithKeyPath:fromValue:toValue:offset:];
+[UIKBKeyViewAnimator normalizedUnwindAnimationWithKeyPath:originallyFromValue:toValue:offset:];
+[UIKBKeyViewAnimator normalizedUnwindOpacityAnimationWithKeyPath:originallyFromValue:toValue:offset:];
```

## Instance methods

```
-[UIKBKeyViewAnimator disabled];
-[UIKBKeyViewAnimator keycapAlternateTransform:];
-[UIKBKeyViewAnimator keycapPrimaryDualStringTransform:];
-[UIKBKeyViewAnimator keycapPrimaryTransform];
-[UIKBKeyViewAnimator keyViewClassForKey:renderTraits:screenTraits:];
-[UIKBKeyViewAnimator keycapRightSelectRightTransform];
-[UIKBKeyViewAnimator reset];
-[UIKBKeyViewAnimator secondaryGlyphNormalizedExitRect];
-[UIKBKeyViewAnimator keycapMeshTransformFromRect:toRect:scale:];
-[UIKBKeyViewAnimator endTransitionForKeyView:];
-[UIKBKeyViewAnimator updateTransitionForKeyView:normalizedDragSize:];
-[UIKBKeyViewAnimator shouldAssertCurrentKeyState:];
-[UIKBKeyViewAnimator keycapLeftSelectPrimaryTransform];
-[UIKBKeyViewAnimator keycapLeftSelectLeftTransform];
-[UIKBKeyViewAnimator shouldTransitionKeyView:fromState:toState:];
-[UIKBKeyViewAnimator _keyViewClassForSpecialtyKey:screenTraits:];
-[UIKBKeyViewAnimator transitionEndedForKeyView:alternateCount:];
-[UIKBKeyViewAnimator setKeyScale:];
-[UIKBKeyViewAnimator keycapLeftTransform];
-[UIKBKeyViewAnimator keycapRightTransform];
-[UIKBKeyViewAnimator keycapAlternateDualStringTransform:];
-[UIKBKeyViewAnimator delayedDeactivationTimeForKeyView:];
-[UIKBKeyViewAnimator _fadeInKeyView:duration:completion:];
-[UIKBKeyViewAnimator keycapRightSelectPrimaryTransform];
-[UIKBKeyViewAnimator keycapNullTransform];
-[UIKBKeyViewAnimator keycapRightSelectLeftTransform];
-[UIKBKeyViewAnimator _fadeOutKeyView:duration:completion:];
-[UIKBKeyViewAnimator shouldPurgeKeyViews];
-[UIKBKeyViewAnimator primaryGlyphNormalizedExitRect];
-[UIKBKeyViewAnimator transitionKeyView:fromState:toState:completion:];
-[UIKBKeyViewAnimator keycapLeftSelectRightTransform];
-[UIKBKeyViewAnimator keycapMeshTransformFromRect:toRect:];
-[UIKBKeyViewAnimator keyScale];
-[UIKBKeyViewAnimator transitionOutKeyView:fromState:toState:completion:];
-[UIKBKeyViewAnimator setDisabled:];
-[UIKBKeyViewAnimator primaryReverseTransform];
-[UIKBKeyViewAnimator keycapPrimaryExitTransform];
-[UIKBKeyViewAnimator transitionStartedForKeyView:alternateCount:toLeft:];
```
