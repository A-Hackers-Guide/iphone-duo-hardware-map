# `_UISystemBannerRequest`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCSecureCoding`
- 6 instance variables, 9 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"_UIOverlayService" _overlayService;
@"NSString" _primaryTitleText;
@"NSString" _secondaryTitleText;
d _preferredMinimumBannerWidth;
d _preferredMaximumBannerWidth;
d _bannerTimeoutDuration;
```

## Properties

```
@property (T@"NSString",&,N,V_primaryTitleText) primaryTitleText;
@property (T@"NSString",&,N,V_secondaryTitleText) secondaryTitleText;
@property (Td,N,V_preferredMinimumBannerWidth) preferredMinimumBannerWidth;
@property (Td,N,V_preferredMaximumBannerWidth) preferredMaximumBannerWidth;
@property (Td,N,V_bannerTimeoutDuration) bannerTimeoutDuration;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UISystemBannerRequest supportsBSXPCSecureCoding];
```

## Instance methods

```
-[_UISystemBannerRequest init];
-[_UISystemBannerRequest encodeWithBSXPCCoder:];
-[_UISystemBannerRequest initWithBSXPCCoder:];
-[_UISystemBannerRequest isEqual:];
-[_UISystemBannerRequest setPreferredMinimumBannerWidth:];
-[_UISystemBannerRequest setPreferredMaximumBannerWidth:];
-[_UISystemBannerRequest bannerTimeoutDuration];
-[_UISystemBannerRequest postBanner];
-[_UISystemBannerRequest preferredMaximumBannerWidth];
-[_UISystemBannerRequest preferredMinimumBannerWidth];
-[_UISystemBannerRequest primaryTitleText];
-[_UISystemBannerRequest secondaryTitleText];
-[_UISystemBannerRequest setBannerTimeoutDuration:];
-[_UISystemBannerRequest setPrimaryTitleText:];
-[_UISystemBannerRequest setSecondaryTitleText:];
-[_UISystemBannerRequest verifyParameters];
```
