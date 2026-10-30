# `TUSubtitleProvider`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"TUCallProviderManager" _callProviderManager;
@"TUMetadataCache" _metadataCache;
@"NSCache" _callProviderCache;
```

## Properties

```
@property (T@"TUCallProviderManager",R,N,V_callProviderManager) callProviderManager;
@property (T@"TUMetadataCache",R,N,V_metadataCache) metadataCache;
@property (T@"NSCache",R,N,V_callProviderCache) callProviderCache;
```

## Instance methods

```
-[TUSubtitleProvider metadataCache];
-[TUSubtitleProvider localizedSubtitleForRecentCall:handle:contact:includeCallNotes:];
-[TUSubtitleProvider callProviderCache];
-[TUSubtitleProvider callProviderForRecentCall:];
-[TUSubtitleProvider callProviderManager];
-[TUSubtitleProvider initWithMetadataCache:callProviderManager:];
-[TUSubtitleProvider localizedSubtitleForRecentCall:handle:contact:];
```
