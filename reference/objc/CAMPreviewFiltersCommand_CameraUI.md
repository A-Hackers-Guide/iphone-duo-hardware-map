# `CAMPreviewFiltersCommand`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMCaptureCommand`
- 4 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
B __styledCaptureAllowed;
B __recording;
@"NSArray" _filters;
q __mode;
```

## Properties

```
@property (Tq,R,N,V__mode) _mode;
@property (TB,R,N,V__styledCaptureAllowed) _styledCaptureAllowed;
@property (TB,R,N,V__recording) _recording;
@property (T@"NSArray",R,N,V_filters) filters;
```

## Instance methods

```
-[CAMPreviewFiltersCommand _mode];
-[CAMPreviewFiltersCommand filters];
-[CAMPreviewFiltersCommand executeWithContext:];
-[CAMPreviewFiltersCommand copyWithZone:];
-[CAMPreviewFiltersCommand _styledCaptureAllowed];
-[CAMPreviewFiltersCommand _recording];
-[CAMPreviewFiltersCommand initWithFilters:captureMode:styledCaptureAllowed:recording:];
-[CAMPreviewFiltersCommand initWithSubcommands:];
```
