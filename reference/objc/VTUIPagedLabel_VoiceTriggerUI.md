# `VTUIPagedLabel`

- Image: [`/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/VoiceTriggerUI`](../userland/System__Library__PrivateFrameworks__VoiceTriggerUI.framework__VoiceTriggerUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 10 instance variables, 0 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"UIScrollView" _scrollView;
@"UIView" _instructionContainerLeft;
@"UIView" _instructionContainerRight;
@"UILabel" _instructionLabelLeft;
@"UILabel" _instructionLabelRight;
B _isProximity;
B _hasIntelligentLight;
Q _slideGeneration;
B _isSliding;
q _enrollmentStyle;
```

## Instance methods

```
-[VTUIPagedLabel clear];
-[VTUIPagedLabel setupViews];
-[VTUIPagedLabel layoutSubviews];
-[VTUIPagedLabel _restingContentOffset];
-[VTUIPagedLabel setText:];
-[VTUIPagedLabel initWithFrame:isProximity:forEnrollmentStyle:];
-[VTUIPagedLabel initWithFrame:isProximity:forEnrollmentStyle:withIntelligentLight:];
-[VTUIPagedLabel slideInText:afterDelay:completion:];
```
