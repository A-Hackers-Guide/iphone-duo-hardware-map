# `UIKBBackgroundView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIKBSplitImageView`
- Protocols: `UIKBCacheableView`
- 14 instance variables, 14 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"UIKBTree" _keyplane;
@"UITextInputTraits" _inputTraits;
i _visualStyle;
@"NSObject" _geometryCacheKey;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _splitLeftRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _splitLeftCacheRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _splitRightRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _splitRightCacheRect;
Q _topCorners;
B _isSplit;
B _centerFilled;
B _hasCandidateKeys;
@"UIKBRenderConfig" _renderConfig;
@"UIKBScreenTraits" _screenTraits;
```

## Properties

```
@property (T@"NSObject",&,N,V_geometryCacheKey) geometryCacheKey;
@property (T@"UIKBScreenTraits",&,N,V_screenTraits) screenTraits;
@property (T@"UIKBRenderConfig",&,N,V_renderConfig) renderConfig;
@property (T@"NSString",R,N) cacheKey;
@property (TB,R,N) cacheDeferable;
@property (Td,R,N) cachedWidth;
@property (TB,R,N) keepNonPersistent;
@property (TB,R,N) displaysColorImage;
@property (Tq,R,N) assetIdiom;
@property (Tq,?,R,N) cacheDeferPriority;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIKBBackgroundView assetIdiom];
-[UIKBBackgroundView renderConfig];
-[UIKBBackgroundView _canDrawContent];
-[UIKBBackgroundView cachedWidth];
-[UIKBBackgroundView setRenderConfig:];
-[UIKBBackgroundView displayLayer:];
-[UIKBBackgroundView drawContentsOfRenderers:];
-[UIKBBackgroundView cacheKey];
-[UIKBBackgroundView setScreenTraits:];
-[UIKBBackgroundView keepNonPersistent];
-[UIKBBackgroundView refreshStyleForKeyplane:inputTraits:];
-[UIKBBackgroundView displaysColorImage];
-[UIKBBackgroundView screenTraits];
-[UIKBBackgroundView cacheKeysForRenderFlags:];
-[UIKBBackgroundView cacheDeferable];
-[UIKBBackgroundView geometryCacheKey];
-[UIKBBackgroundView setGeometryCacheKey:];
-[UIKBBackgroundView initWithFrame:];
```
