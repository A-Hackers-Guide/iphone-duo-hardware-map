# `NWURLError`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSError`
- 13 instance variables, 13 properties, 40 instance methods, 2 class methods

## Instance variables

```
@"NSError" _underlyingError;
@"NSURL" _failingURL;
^{__SecTrust=} _peerTrust;
@"NSNumber" _networkUnavailableReason;
@"NSNumber" _backgroundTaskCancelledReason;
@"NSNumber" _webSocketHandshakeFailureReason;
@"NSNumber" _privacyProxyFailure;
@"NSNumber" _vpnInactiveFailure;
@"NSNumber" _blockedTrackerFailure;
@"NSObject<OS_nw_path>" _path;
@"NSObject<OS_nw_resolution_report>" _resolutionReport;
@"NSData" _downloadTaskResumeData;
@"NSData" _uploadTaskResumeData;
```

## Properties

```
@property (T@"NSError",&,N,V_underlyingError) underlyingError;
@property (T@"NSURL",&,N,V_failingURL) failingURL;
@property (T^{__SecTrust=},&,N,V_peerTrust) peerTrust;
@property (T@"NSNumber",&,N,V_networkUnavailableReason) networkUnavailableReason;
@property (T@"NSNumber",&,N,V_backgroundTaskCancelledReason) backgroundTaskCancelledReason;
@property (T@"NSNumber",&,N,V_webSocketHandshakeFailureReason) webSocketHandshakeFailureReason;
@property (T@"NSNumber",&,N,V_privacyProxyFailure) privacyProxyFailure;
@property (T@"NSNumber",&,N,V_vpnInactiveFailure) vpnInactiveFailure;
@property (T@"NSNumber",&,N,V_blockedTrackerFailure) blockedTrackerFailure;
@property (T@"NSObject<OS_nw_path>",&,N,V_path) path;
@property (T@"NSObject<OS_nw_resolution_report>",&,N,V_resolutionReport) resolutionReport;
@property (T@"NSData",&,N,V_downloadTaskResumeData) downloadTaskResumeData;
@property (T@"NSData",&,N,V_uploadTaskResumeData) uploadTaskResumeData;
```

## Class methods

```
+[NWURLError supportsSecureCoding];
+[NWURLError allUserInfoKeys];
```

## Instance methods

```
-[NWURLError localizedDescription];
-[NWURLError peerTrust];
-[NWURLError resolutionReport];
-[NWURLError setDownloadTaskResumeData:];
-[NWURLError setUnderlyingError:];
-[NWURLError localizedFailureReason];
-[NWURLError localizedRecoverySuggestion];
-[NWURLError downloadTaskResumeData];
-[NWURLError userInfo];
-[NWURLError dealloc];
-[NWURLError fillErrorForLoader:andTask:];
-[NWURLError setPeerTrust:];
-[NWURLError setFailingURL:];
-[NWURLError setBlockedTrackerFailure:];
-[NWURLError translateDNSError:];
-[NWURLError webSocketHandshakeFailureReason];
-[NWURLError setResolutionReport:];
-[NWURLError translateCodeForError:];
-[NWURLError setVpnInactiveFailure:];
-[NWURLError translatePOSIXError:];
-[NWURLError blockedTrackerFailure];
-[NWURLError vpnInactiveFailure];
-[NWURLError initWithErrorCode:];
-[NWURLError encodeWithCoder:];
-[NWURLError underlyingError];
-[NWURLError uploadTaskResumeData];
-[NWURLError backgroundTaskCancelledReason];
-[NWURLError setBackgroundTaskCancelledReason:];
-[NWURLError setPrivacyProxyFailure:];
-[NWURLError initWithCoder:];
-[NWURLError setPath:];
-[NWURLError privacyProxyFailure];
-[NWURLError copyWithZone:];
-[NWURLError networkUnavailableReason];
-[NWURLError setUploadTaskResumeData:];
-[NWURLError setNetworkUnavailableReason:];
-[NWURLError setWebSocketHandshakeFailureReason:];
-[NWURLError translateTLSError:];
-[NWURLError path];
-[NWURLError failingURL];
```
