# `CAMSlashContainer`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `CAMViewOrientable`
- 6 instance variables, 10 properties, 20 instance methods, 0 class methods

## Instance variables

```
B _slashed;
q _orientation;
@"UIView" _contentView;
@"CAMSlashView" __slashView;
@"CAMSlashMaskView" __slashMaskView;
{CGSize="width"d"height"d} _slashSize;
```

## Properties

```
@property (T@"CAMSlashView",&,N,S_setSlashView:,V__slashView) _slashView;
@property (T@"CAMSlashMaskView",&,N,S_setSlashMaskView:,V__slashMaskView) _slashMaskView;
@property (T@"UIView",&,N,V_contentView) contentView;
@property (TB,N,GisSlashed,V_slashed) slashed;
@property (T{CGSize=dd},N,V_slashSize) slashSize;
@property (Tq,N,V_orientation) orientation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAMSlashContainer setOrientation:animated:];
-[CAMSlashContainer setOrientation:];
-[CAMSlashContainer setContentView:];
-[CAMSlashContainer intrinsicContentSize];
-[CAMSlashContainer alignmentRectInsets];
-[CAMSlashContainer _setSlashView:];
-[CAMSlashContainer setSlashed:animated:];
-[CAMSlashContainer orientation];
-[CAMSlashContainer layoutSubviews];
-[CAMSlashContainer _slashView];
-[CAMSlashContainer _updateOrientationAnimated:];
-[CAMSlashContainer setSlashSize:];
-[CAMSlashContainer isSlashed];
-[CAMSlashContainer _setSlashMaskView:];
-[CAMSlashContainer contentView];
-[CAMSlashContainer _updateSlashAnimated:];
-[CAMSlashContainer slashSize];
-[CAMSlashContainer _slashMaskView];
-[CAMSlashContainer setSlashed:];
-[CAMSlashContainer initWithFrame:];
```
