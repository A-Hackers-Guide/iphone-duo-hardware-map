# `DCNotesTextureBackgroundView`

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 4 instance variables, 4 properties, 15 instance methods, 2 class methods

## Instance variables

```
B _scrollsTexture;
@"DCNotesTextureView" _textureView;
@"NSLayoutConstraint" _textureYConstraint;
@"NSLayoutConstraint" _textureHeightConstraint;
```

## Properties

```
@property (T@"NSLayoutConstraint",&,N,V_textureYConstraint) textureYConstraint;
@property (T@"NSLayoutConstraint",&,N,V_textureHeightConstraint) textureHeightConstraint;
@property (T@"DCNotesTextureView",R,N,V_textureView) textureView;
@property (TB,V_scrollsTexture) scrollsTexture;
```

## Class methods

```
+[DCNotesTextureBackgroundView textureImage];
+[DCNotesTextureBackgroundView colorWithPaperTexturePatternImage];
```

## Instance methods

```
-[DCNotesTextureBackgroundView setContentOffset:];
-[DCNotesTextureBackgroundView setBounds:];
-[DCNotesTextureBackgroundView setFrame:];
-[DCNotesTextureBackgroundView initWithCoder:];
-[DCNotesTextureBackgroundView textureView];
-[DCNotesTextureBackgroundView initWithFrame:];
-[DCNotesTextureBackgroundView commonInitWithScrollingTextures:hasAlpha:];
-[DCNotesTextureBackgroundView heightByCoveringHeight:withImage:];
-[DCNotesTextureBackgroundView initWithFrame:scrollingTextures:hasAlpha:];
-[DCNotesTextureBackgroundView scrollsTexture];
-[DCNotesTextureBackgroundView setScrollsTexture:];
-[DCNotesTextureBackgroundView setTextureHeightConstraint:];
-[DCNotesTextureBackgroundView setTextureYConstraint:];
-[DCNotesTextureBackgroundView textureHeightConstraint];
-[DCNotesTextureBackgroundView textureYConstraint];
```
