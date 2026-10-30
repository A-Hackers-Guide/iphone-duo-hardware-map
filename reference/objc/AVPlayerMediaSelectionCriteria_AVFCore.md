# `AVPlayerMediaSelectionCriteria`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 3 properties, 22 instance methods, 0 class methods

## Instance variables

```
^v _criteriaInternal;
```

## Properties

```
@property (T@"NSArray",R,N) preferredLanguages;
@property (T@"NSArray",R,N) preferredMediaCharacteristics;
@property (T@"NSArray",R,N) principalMediaCharacteristics;
```

## Instance methods

```
-[AVPlayerMediaSelectionCriteria preferredLanguages];
-[AVPlayerMediaSelectionCriteria init];
-[AVPlayerMediaSelectionCriteria dealloc];
-[AVPlayerMediaSelectionCriteria description];
-[AVPlayerMediaSelectionCriteria _fallbackPreferredLanguages];
-[AVPlayerMediaSelectionCriteria _fallbackPreferredMediaCharacteristics];
-[AVPlayerMediaSelectionCriteria _precludedMediaCharacteristics];
-[AVPlayerMediaSelectionCriteria figDictionary];
-[AVPlayerMediaSelectionCriteria initWithFigDictionary:];
-[AVPlayerMediaSelectionCriteria initWithPreferredLanguages:preferredMediaCharacteristics:];
-[AVPlayerMediaSelectionCriteria initWithPreferredLanguages:preferredMediaCharacteristics:fallbackPreferredLanguages:fallbackPreferredMediaCharacteristics:captionDisplayType:];
-[AVPlayerMediaSelectionCriteria initWithPreferredLanguages:preferredMediaCharacteristics:preferredMediaSubTypes:precludedMediaSubTypes:];
-[AVPlayerMediaSelectionCriteria initWithPreferredLanguages:preferredMediaCharacteristics:preferredMediaSubTypes:precludedMediaSubTypes:preferMultichannelAudio:precludeMultichannelAudio:];
-[AVPlayerMediaSelectionCriteria initWithPremiumMediaCharacteristics:preferredLanguages:preferredMediaCharacteristics:];
-[AVPlayerMediaSelectionCriteria initWithPrincipalMediaCharacteristics:preferredLanguages:preferredMediaCharacteristics:];
-[AVPlayerMediaSelectionCriteria precludeMultichannelAudio];
-[AVPlayerMediaSelectionCriteria precludedMediaSubTypes];
-[AVPlayerMediaSelectionCriteria preferMultichannelAudio];
-[AVPlayerMediaSelectionCriteria preferredMediaCharacteristics];
-[AVPlayerMediaSelectionCriteria preferredMediaSubTypes];
-[AVPlayerMediaSelectionCriteria premiumMediaCharacteristics];
-[AVPlayerMediaSelectionCriteria principalMediaCharacteristics];
```
