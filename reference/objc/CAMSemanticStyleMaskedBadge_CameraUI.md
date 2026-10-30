# `CAMSemanticStyleMaskedBadge`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 6 instance variables, 6 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"CEKBadgeTextView" _badgeView;
@"<CEKCaptureStyle>" _semanticStyle;
d _badgeLeftInset;
q _orientation;
@"NSTimer" __badgeUpdateLockoutTimer;
@"NSString" __cachedText;
```

## Properties

```
@property (T@"NSTimer",&,N,V__badgeUpdateLockoutTimer) _badgeUpdateLockoutTimer;
@property (T@"NSString",&,N,V__cachedText) _cachedText;
@property (T@"CEKBadgeTextView",R,N,V_badgeView) badgeView;
@property (T@"<CEKCaptureStyle>",&,N,V_semanticStyle) semanticStyle;
@property (Td,N,V_badgeLeftInset) badgeLeftInset;
@property (Tq,N,V_orientation) orientation;
```

## Instance methods

```
-[CAMSemanticStyleMaskedBadge setOrientation:];
-[CAMSemanticStyleMaskedBadge setSemanticStyle:];
-[CAMSemanticStyleMaskedBadge intrinsicContentSize];
-[CAMSemanticStyleMaskedBadge badgeView];
-[CAMSemanticStyleMaskedBadge orientation];
-[CAMSemanticStyleMaskedBadge layoutSubviews];
-[CAMSemanticStyleMaskedBadge sizeThatFits:];
-[CAMSemanticStyleMaskedBadge semanticStyle];
-[CAMSemanticStyleMaskedBadge initWithFrame:];
-[CAMSemanticStyleMaskedBadge setSemanticStyle:delayIfNeeded:];
-[CAMSemanticStyleMaskedBadge set_cachedText:];
-[CAMSemanticStyleMaskedBadge _badgeUpdateLockoutTimer];
-[CAMSemanticStyleMaskedBadge _cachedText];
-[CAMSemanticStyleMaskedBadge _handleBadgeUpdateLockoutTimerFired:];
-[CAMSemanticStyleMaskedBadge _requestTextUpdateDelayIfNeeded:];
-[CAMSemanticStyleMaskedBadge badgeLeftInset];
-[CAMSemanticStyleMaskedBadge setBadgeLeftInset:];
-[CAMSemanticStyleMaskedBadge set_badgeUpdateLockoutTimer:];
```
