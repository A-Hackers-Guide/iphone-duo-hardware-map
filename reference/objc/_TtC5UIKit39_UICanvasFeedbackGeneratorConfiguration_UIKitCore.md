# `_TtC5UIKit39_UICanvasFeedbackGeneratorConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIFeedbackGeneratorConfiguration`
- 5 instance variables, 9 properties, 18 instance methods, 1 class methods

## Instance variables

```
(objc_protocol 0x186443248) _$s_So11_UIFeedbackCXcSg _snappingFeedback;
(objc_protocol 0x186443248) _$s_So11_UIFeedbackCXcSg _pathCompletingFeedback;
_$sSS snappingFeedbackPatternName;
_$sSS snappingTrackpadFeedbackPatternName;
_$sSS pathCompletingFeedbackPatternName;
```

## Properties

```
@property (T@"_UIFeedback<_UIFeedbackDiscretePlayable>",N,&) snappingFeedback;
@property (T@"_UIFeedback<_UIFeedbackDiscretePlayable>",N,&) pathCompletingFeedback;
@property (T@"NSArray",N,R) feedbackKeyPaths;
@property (Tq,N) requiredSupportLevel;
@property (Tq,N) requiredPeripheralSupportLevel;
@property (T@"NSString",N,C) snappingFeedbackPatternName;
@property (T@"NSString",N,C) snappingTrackpadFeedbackPatternName;
@property (T@"NSString",N,C) pathCompletingFeedbackPatternName;
@property (T@"NSArray",N,R) hidFeedbackPatternNameKeyPaths;
```

## Class methods

```
+[_TtC5UIKit39_UICanvasFeedbackGeneratorConfiguration defaultConfiguration];
```

## Instance methods

```
-[_TtC5UIKit39_UICanvasFeedbackGeneratorConfiguration init];
-[_TtC5UIKit39_UICanvasFeedbackGeneratorConfiguration feedbackKeyPaths];
-[_TtC5UIKit39_UICanvasFeedbackGeneratorConfiguration requiredPeripheralSupportLevel];
-[_TtC5UIKit39_UICanvasFeedbackGeneratorConfiguration _alternateFeedback:forDevice:senderID:];
-[_TtC5UIKit39_UICanvasFeedbackGeneratorConfiguration hidFeedbackPatternNameKeyPaths];
-[_TtC5UIKit39_UICanvasFeedbackGeneratorConfiguration requiredSupportLevel];
-[_TtC5UIKit39_UICanvasFeedbackGeneratorConfiguration setSnappingFeedbackPatternName:];
-[_TtC5UIKit39_UICanvasFeedbackGeneratorConfiguration pathCompletingFeedback];
-[_TtC5UIKit39_UICanvasFeedbackGeneratorConfiguration pathCompletingFeedbackPatternName];
-[_TtC5UIKit39_UICanvasFeedbackGeneratorConfiguration setPathCompletingFeedback:];
-[_TtC5UIKit39_UICanvasFeedbackGeneratorConfiguration setPathCompletingFeedbackPatternName:];
-[_TtC5UIKit39_UICanvasFeedbackGeneratorConfiguration setRequiredPeripheralSupportLevel:];
-[_TtC5UIKit39_UICanvasFeedbackGeneratorConfiguration setRequiredSupportLevel:];
-[_TtC5UIKit39_UICanvasFeedbackGeneratorConfiguration setSnappingFeedback:];
-[_TtC5UIKit39_UICanvasFeedbackGeneratorConfiguration setSnappingTrackpadFeedbackPatternName:];
-[_TtC5UIKit39_UICanvasFeedbackGeneratorConfiguration snappingFeedback];
-[_TtC5UIKit39_UICanvasFeedbackGeneratorConfiguration snappingFeedbackPatternName];
-[_TtC5UIKit39_UICanvasFeedbackGeneratorConfiguration snappingTrackpadFeedbackPatternName];
```
