# `_UIEdgeFeedbackGeneratorConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIFeedbackGeneratorUserInteractionDrivenConfiguration`
- 13 instance variables, 13 properties, 31 instance methods, 7 class methods

## Instance variables

```
@"_UIFeedback<_UIFeedbackDiscretePlayable>" _userInteractingThresholdFeedback;
@? _userInteractingThresholdFeedbackUpdateBlock;
@"_UIFeedback<_UIFeedbackContinuousPlayable>" _userInteractingBeyondEdgeFeedback;
@? _userInteractingBeyondEdgeFeedbackUpdateBlock;
@"_UIFeedback<_UIFeedbackDiscretePlayable>" _userInteractingReleaseFeedback;
@? _userInteractingReleaseFeedbackUpdateBlock;
@"_UIFeedback<_UIFeedbackDiscretePlayable>" _animatingThresholdFeedback;
@? _animatingThresholdFeedbackUpdateBlock;
@"_UIFeedback<_UIFeedbackDiscretePlayable>" _animatingMaximumExtentFeedback;
@? _animatingMaximumExtentFeedbackUpdateBlock;
@"NSString" _hidFeedbackPatternName;
q _defaultAxis;
d _minDistanceFromEdge;
```

## Properties

```
@property (Tq,N,G_defaultAxis,S_setDefaultAxis:,V_defaultAxis) defaultAxis;
@property (Td,N,V_minDistanceFromEdge) minDistanceFromEdge;
@property (T@"_UIFeedback<_UIFeedbackDiscretePlayable>",&,N,V_userInteractingThresholdFeedback) userInteractingThresholdFeedback;
@property (T@?,C,N,V_userInteractingThresholdFeedbackUpdateBlock) userInteractingThresholdFeedbackUpdateBlock;
@property (T@"_UIFeedback<_UIFeedbackContinuousPlayable>",&,N,V_userInteractingBeyondEdgeFeedback) userInteractingBeyondEdgeFeedback;
@property (T@?,C,N,V_userInteractingBeyondEdgeFeedbackUpdateBlock) userInteractingBeyondEdgeFeedbackUpdateBlock;
@property (T@"_UIFeedback<_UIFeedbackDiscretePlayable>",&,N,V_userInteractingReleaseFeedback) userInteractingReleaseFeedback;
@property (T@?,C,N,V_userInteractingReleaseFeedbackUpdateBlock) userInteractingReleaseFeedbackUpdateBlock;
@property (T@"_UIFeedback<_UIFeedbackDiscretePlayable>",&,N,V_animatingThresholdFeedback) animatingThresholdFeedback;
@property (T@?,C,N,V_animatingThresholdFeedbackUpdateBlock) animatingThresholdFeedbackUpdateBlock;
@property (T@"_UIFeedback<_UIFeedbackDiscretePlayable>",&,N,V_animatingMaximumExtentFeedback) animatingMaximumExtentFeedback;
@property (T@?,C,N,V_animatingMaximumExtentFeedbackUpdateBlock) animatingMaximumExtentFeedbackUpdateBlock;
@property (T@"NSString",&,N,V_hidFeedbackPatternName) hidFeedbackPatternName;
```

## Class methods

```
+[_UIEdgeFeedbackGeneratorConfiguration horizontalScrollConfiguration];
+[_UIEdgeFeedbackGeneratorConfiguration _zoomConfiguration];
+[_UIEdgeFeedbackGeneratorConfiguration verticalScrollConfiguration];
+[_UIEdgeFeedbackGeneratorConfiguration sliderConfiguration];
+[_UIEdgeFeedbackGeneratorConfiguration swipePresentationConfiguration];
+[_UIEdgeFeedbackGeneratorConfiguration _scrollConfigurationWithAxis:];
+[_UIEdgeFeedbackGeneratorConfiguration defaultConfiguration];
```

## Instance methods

```
-[_UIEdgeFeedbackGeneratorConfiguration setAnimatingThresholdFeedbackUpdateBlock:];
-[_UIEdgeFeedbackGeneratorConfiguration setUserInteractingThresholdFeedback:];
-[_UIEdgeFeedbackGeneratorConfiguration minDistanceFromEdge];
-[_UIEdgeFeedbackGeneratorConfiguration feedbackKeyPaths];
-[_UIEdgeFeedbackGeneratorConfiguration animatingMaximumExtentFeedback];
-[_UIEdgeFeedbackGeneratorConfiguration _alternateFeedback:forDevice:senderID:];
-[_UIEdgeFeedbackGeneratorConfiguration userInteractingReleaseFeedback];
-[_UIEdgeFeedbackGeneratorConfiguration setAnimatingMaximumExtentFeedback:];
-[_UIEdgeFeedbackGeneratorConfiguration setHidFeedbackPatternName:];
-[_UIEdgeFeedbackGeneratorConfiguration setUserInteractingReleaseFeedback:];
-[_UIEdgeFeedbackGeneratorConfiguration userInteractingThresholdFeedback];
-[_UIEdgeFeedbackGeneratorConfiguration setMinDistanceFromEdge:];
-[_UIEdgeFeedbackGeneratorConfiguration setUserInteractingBeyondEdgeFeedback:];
-[_UIEdgeFeedbackGeneratorConfiguration setUserInteractingReleaseFeedbackUpdateBlock:];
-[_UIEdgeFeedbackGeneratorConfiguration userInteractingBeyondEdgeFeedback];
-[_UIEdgeFeedbackGeneratorConfiguration userInteractingThresholdFeedbackUpdateBlock];
-[_UIEdgeFeedbackGeneratorConfiguration _defaultAxis];
-[_UIEdgeFeedbackGeneratorConfiguration hidFeedbackPatternNameKeyPaths];
-[_UIEdgeFeedbackGeneratorConfiguration animatingThresholdFeedback];
-[_UIEdgeFeedbackGeneratorConfiguration hidFeedbackPatternName];
-[_UIEdgeFeedbackGeneratorConfiguration animatingThresholdFeedbackUpdateBlock];
-[_UIEdgeFeedbackGeneratorConfiguration requiredSupportLevel];
-[_UIEdgeFeedbackGeneratorConfiguration setUserInteractingThresholdFeedbackUpdateBlock:];
-[_UIEdgeFeedbackGeneratorConfiguration copyWithZone:];
-[_UIEdgeFeedbackGeneratorConfiguration animatingMaximumExtentFeedbackUpdateBlock];
-[_UIEdgeFeedbackGeneratorConfiguration userInteractingBeyondEdgeFeedbackUpdateBlock];
-[_UIEdgeFeedbackGeneratorConfiguration setAnimatingMaximumExtentFeedbackUpdateBlock:];
-[_UIEdgeFeedbackGeneratorConfiguration _setDefaultAxis:];
-[_UIEdgeFeedbackGeneratorConfiguration userInteractingReleaseFeedbackUpdateBlock];
-[_UIEdgeFeedbackGeneratorConfiguration setUserInteractingBeyondEdgeFeedbackUpdateBlock:];
-[_UIEdgeFeedbackGeneratorConfiguration setAnimatingThresholdFeedback:];
```
