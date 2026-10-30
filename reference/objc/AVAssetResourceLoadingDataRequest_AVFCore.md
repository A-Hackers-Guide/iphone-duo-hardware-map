# `AVAssetResourceLoadingDataRequest`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"AVAssetResourceLoadingDataRequestInternal" _dataRequest;
```

## Properties

```
@property (Tq,R,N) requestedOffset;
@property (Tq,R,N) requestedLength;
@property (TB,R,N) requestsAllDataToEndOfResource;
@property (Tq,R,N) currentOffset;
```

## Instance methods

```
-[AVAssetResourceLoadingDataRequest init];
-[AVAssetResourceLoadingDataRequest dealloc];
-[AVAssetResourceLoadingDataRequest currentOffset];
-[AVAssetResourceLoadingDataRequest _requestInfo];
-[AVAssetResourceLoadingDataRequest description];
-[AVAssetResourceLoadingDataRequest _loadingRequest];
-[AVAssetResourceLoadingDataRequest requestedOffset];
-[AVAssetResourceLoadingDataRequest requestedLength];
-[AVAssetResourceLoadingDataRequest initWithLoadingRequest:requestedOffset:requestedLength:requestsAllDataToEndOfResource:canSupplyIncrementalDataImmediately:];
-[AVAssetResourceLoadingDataRequest requestsAllDataToEndOfResource];
-[AVAssetResourceLoadingDataRequest respondWithData:];
```
