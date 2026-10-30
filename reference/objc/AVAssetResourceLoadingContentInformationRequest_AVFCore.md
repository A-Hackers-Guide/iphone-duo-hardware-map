# `AVAssetResourceLoadingContentInformationRequest`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 6 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"AVAssetResourceLoadingContentInformationRequestInternal" _contentInformationRequest;
```

## Properties

```
@property (T@"NSString",C,N) contentType;
@property (T@"NSArray",R,N) allowedContentTypes;
@property (Tq,N) contentLength;
@property (TB,N,GisByteRangeAccessSupported) byteRangeAccessSupported;
@property (T@"NSDate",C,N) renewalDate;
@property (TB,N,GisEntireLengthAvailableOnDemand) entireLengthAvailableOnDemand;
```

## Instance methods

```
-[AVAssetResourceLoadingContentInformationRequest setContentType:];
-[AVAssetResourceLoadingContentInformationRequest contentLength];
-[AVAssetResourceLoadingContentInformationRequest propertyList];
-[AVAssetResourceLoadingContentInformationRequest init];
-[AVAssetResourceLoadingContentInformationRequest contentType];
-[AVAssetResourceLoadingContentInformationRequest dealloc];
-[AVAssetResourceLoadingContentInformationRequest description];
-[AVAssetResourceLoadingContentInformationRequest allowedContentTypes];
-[AVAssetResourceLoadingContentInformationRequest setRenewalDate:];
-[AVAssetResourceLoadingContentInformationRequest isEntireLengthAvailableOnDemand];
-[AVAssetResourceLoadingContentInformationRequest initWithLoadingRequest:allowedContentTypes:];
-[AVAssetResourceLoadingContentInformationRequest isByteRangeAccessSupported];
-[AVAssetResourceLoadingContentInformationRequest isDiskCachingPermitted];
-[AVAssetResourceLoadingContentInformationRequest renewalDate];
-[AVAssetResourceLoadingContentInformationRequest setByteRangeAccessSupported:];
-[AVAssetResourceLoadingContentInformationRequest setContentLength:];
-[AVAssetResourceLoadingContentInformationRequest setDiskCachingPermitted:];
-[AVAssetResourceLoadingContentInformationRequest setEntireLengthAvailableOnDemand:];
```
