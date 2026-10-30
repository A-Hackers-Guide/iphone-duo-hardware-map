# `SBPIPContentViewLayoutContext`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 10 properties, 23 instance methods, 0 class methods

## Instance variables

```
B _sizeChanged;
d _currentAspectRatio;
d _currentSize;
d _minimumSizePreference;
d _defaultSizePreference;
d _maximumSizePreference;
d _minimumSizeSpanBetweenPreferredSizes;
d _maximumSizeSpanForPreferredSizeTuning;
@"SBPIPDefaults" _defaults;
@"NSString" _contentTypeIdentifier;
```

## Properties

```
@property (Td,N,V_currentAspectRatio) currentAspectRatio;
@property (Td,N,V_currentSize) currentSize;
@property (TB,R,N,GhasSizeChanged,V_sizeChanged) sizeChanged;
@property (Td,N,V_minimumSizePreference) minimumSizePreference;
@property (Td,N,V_defaultSizePreference) defaultSizePreference;
@property (Td,N,V_maximumSizePreference) maximumSizePreference;
@property (Td,N,V_minimumSizeSpanBetweenPreferredSizes) minimumSizeSpanBetweenPreferredSizes;
@property (Td,N,V_maximumSizeSpanForPreferredSizeTuning) maximumSizeSpanForPreferredSizeTuning;
@property (T@"SBPIPDefaults",&,N,V_defaults) defaults;
@property (T@"NSString",C,N,V_contentTypeIdentifier) contentTypeIdentifier;
```

## Instance methods

```
-[SBPIPContentViewLayoutContext setDefaults:];
-[SBPIPContentViewLayoutContext defaults];
-[SBPIPContentViewLayoutContext contentTypeIdentifier];
-[SBPIPContentViewLayoutContext currentSize];
-[SBPIPContentViewLayoutContext currentAspectRatio];
-[SBPIPContentViewLayoutContext setCurrentSize:];
-[SBPIPContentViewLayoutContext defaultSizePreference];
-[SBPIPContentViewLayoutContext hasSizeChanged];
-[SBPIPContentViewLayoutContext initWithPlatformMetrics:contentSize:defaults:];
-[SBPIPContentViewLayoutContext maximumSizePreference];
-[SBPIPContentViewLayoutContext maximumSizeSpanForPreferredSizeTuning];
-[SBPIPContentViewLayoutContext minimumSizePreference];
-[SBPIPContentViewLayoutContext minimumSizeSpanBetweenPreferredSizes];
-[SBPIPContentViewLayoutContext setContentTypeIdentifier:];
-[SBPIPContentViewLayoutContext setCurrentAspectRatio:];
-[SBPIPContentViewLayoutContext setCurrentSize:forAspectRatio:];
-[SBPIPContentViewLayoutContext setCurrentSize:forAspectRatio:persistingLastKnownSize:];
-[SBPIPContentViewLayoutContext setDefaultSizePreference:];
-[SBPIPContentViewLayoutContext setMaximumSizePreference:];
-[SBPIPContentViewLayoutContext setMaximumSizeSpanForPreferredSizeTuning:];
-[SBPIPContentViewLayoutContext setMinimumSizePreference:];
-[SBPIPContentViewLayoutContext setMinimumSizeSpanBetweenPreferredSizes:];
-[SBPIPContentViewLayoutContext updatePlatformMetrics:];
```
