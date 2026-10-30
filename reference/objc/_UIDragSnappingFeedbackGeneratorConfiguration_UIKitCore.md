# `_UIDragSnappingFeedbackGeneratorConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIDragFeedbackGeneratorConfiguration`
- 2 instance variables, 2 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"_UIFeedback<_UIFeedbackDiscretePlayable>" _objectSnappedFeedback;
@"NSString" _hidObjectSnappedFeedbackPatternName;
```

## Properties

```
@property (T@"_UIFeedback<_UIFeedbackDiscretePlayable>",&,N,V_objectSnappedFeedback) objectSnappedFeedback;
@property (T@"NSString",&,N,V_hidObjectSnappedFeedbackPatternName) hidObjectSnappedFeedbackPatternName;
```

## Class methods

```
+[_UIDragSnappingFeedbackGeneratorConfiguration defaultConfiguration];
```

## Instance methods

```
-[_UIDragSnappingFeedbackGeneratorConfiguration hidObjectSnappedFeedbackPatternName];
-[_UIDragSnappingFeedbackGeneratorConfiguration feedbackKeyPaths];
-[_UIDragSnappingFeedbackGeneratorConfiguration _alternateFeedback:forDevice:senderID:];
-[_UIDragSnappingFeedbackGeneratorConfiguration setObjectSnappedFeedback:];
-[_UIDragSnappingFeedbackGeneratorConfiguration setHidObjectSnappedFeedbackPatternName:];
-[_UIDragSnappingFeedbackGeneratorConfiguration objectSnappedFeedback];
-[_UIDragSnappingFeedbackGeneratorConfiguration hidFeedbackPatternNameKeyPaths];
```
