# `THClient`

- Image: [`/System/Library/Frameworks/ThreadNetwork.framework/ThreadNetwork`](../userland/System__Library__Frameworks__ThreadNetwork.framework__ThreadNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 6 properties, 93 instance methods, 0 class methods

## Instance variables

```
B _isConnected;
@"NSXPCConnection" _xpcConnection;
^{dispatch_queue_s=} _threadSafePropertyQueue;
^{dispatch_queue_s=} _apiCAQueue;
@"NSString" _mAppTeamID;
@"NSString" _mAppName;
@"NSString" _mAppBundleID;
```

## Properties

```
@property (T@"NSXPCConnection",&,N,V_xpcConnection) xpcConnection;
@property (T^{dispatch_queue_s=},N,V_threadSafePropertyQueue) threadSafePropertyQueue;
@property (T^{dispatch_queue_s=},V_apiCAQueue) apiCAQueue;
@property (T@"NSString",&,V_mAppTeamID) mAppTeamID;
@property (T@"NSString",&,V_mAppName) mAppName;
@property (T@"NSString",&,V_mAppBundleID) mAppBundleID;
```

## Instance methods

```
-[THClient getTheProxyWithResultBlockCompletion:];
-[THClient isConnected];
-[THClient getTheProxyWithTHCredsParameterCompletion:];
-[THClient getTheProxyWithBoolCompletion:];
-[THClient handleXPCConnectionInvalidated];
-[THClient initCommon];
-[THClient setThreadSafePropertyQueue:];
-[THClient ctcsRetrieveActiveDataSetRecordWithUniqueIdentifier:completion:];
-[THClient retrieveActiveDataSetRecordInternallyForExtendedPANID:completion:];
-[THClient pingXPCServiceWithClientProxy:completion:];
-[THClient init];
-[THClient isPreferredNetworkAvailableWithCompletion:];
-[THClient setXpcConnection:];
-[THClient getAppBundleID];
-[THClient retrieveActiveCredentialsForNearbyNetworksInternallyWithCompletion:];
-[THClient storeCredentialsForBorderAgentInternally:networkName:extendedPANId:activeOperationalDataSet:teamID:completion:];
-[THClient ctcsAddPreferredNetworkWithCompletionInternally:extendedPANId:borderAgentID:ipV4NwSignature:ipv6NwSignature:wifiSSID:wifiPassword:completion:];
-[THClient mAppBundleID];
-[THClient mAppTeamID];
-[THClient retrievePreferredNetworkWithNoScan:];
-[THClient logAPIMetric:withError:isSuccess:isInternal:];
-[THClient dealloc];
-[THClient getAppName];
-[THClient pingXPCService];
-[THClient rapportSendForPreferredNetworkWithMessage:completion:];
-[THClient getTheProxyWithRecordCompletion:];
-[THClient synchronousRemoteObjectProxy];
-[THClient retrievePreferredCredentials:];
-[THClient storeCachedAODasPreferredNetwork:completion:];
-[THClient getConnectionEntitlementValidity];
-[THClient initWithKeychainAccessGroup:];
-[THClient retrieveAllActiveCredentials:];
-[THClient mAppName];
-[THClient ctcsDeleteActiveDataSetRecordWithUniqueIdentifier:completion:];
-[THClient xpcConnection];
-[THClient updatePreferredCredentialsInternally:];
-[THClient deleteCredentialsForBorderAgent:completion:];
-[THClient getTheProxyWithTHCredsAndUuidParametersCompletion:];
-[THClient startThreadBRScanInternally:];
-[THClient validateAODInternally:completion:];
-[THClient invalidate];
-[THClient retrieveAllCredentials:];
-[THClient rapportBrowseForPreferredNetworkWithCompletion:];
-[THClient retrieveOrGeneratePreferredNetworkInternally:];
-[THClient CAInitDispatchQueue];
-[THClient setMAppBundleID:];
-[THClient setMAppTeamID:];
-[THClient ctcsRetrieveOrGeneratePreferredNetworkInternallyWithCompletion:];
-[THClient performXPCRequestBlock:timeout:error:];
-[THClient countNonAppleRecordsWithCompletion:];
-[THClient ctcsCleanKeychainThreadNetworksWithCompletion:];
-[THClient clientProxyWithErrorHandler:];
-[THClient checkPreferredNetworkForActiveOperationalDataset:completion:];
-[THClient storeCredentialsForBorderAgent:activeOperationalDataSet:completion:];
-[THClient initCommonForThreadradiodDataset];
-[THClient getAppTeamID];
-[THClient connectToXPCService];
-[THClient rapportConnectForPreferredNetworkWithCompletion:];
-[THClient retrieveCredentialsForExtendedPANID:completion:];
-[THClient initCommon:];
-[THClient setMAppName:];
-[THClient ctcsRetrievePreferredNetworkInternallyWithCompletion:];
-[THClient ctcsDeletePreferredNetworkForNetworkSignatureInternallyWithCompletion:extendedPANId:ipV4NwSignature:ipv6NwSignature:wifiSSID:completion:];
-[THClient ctcsCleanPreferredAndFrozenThreadNetworksWithCompletion:];
-[THClient clientProxyWithErrorHandler:pingService:];
-[THClient setApiCAQueue:];
-[THClient getConnectionEntitlementValidity:];
-[THClient retrieveCredentialsForUUID:completion:];
-[THClient countPreferredFrozenRecordsWithCompletion:];
-[THClient asynchronousRemoteObjectProxyWithErrorHandler:];
-[THClient currentEnvironment];
-[THClient getTheProxyWithNwSignatureCompletion:];
-[THClient getAppAccessGroup];
-[THClient setIsConnected:];
-[THClient apiCAQueue];
-[THClient ctcsStoreThreadNetworkCredentialActiveDataSetInternally:network:credentialsDataSet:waitForSync:completion:];
-[THClient synchronousClientProxyWithErrorHandler:];
-[THClient handleXPCConnectionInterrupted];
-[THClient getTheProxyWithSetOfTHCredsParameterCompletion:];
-[THClient enableCredentialSharingModeInternallyForExtendedPANID:completion:];
-[THClient retrieveNetworkSignatureWithCompletion:];
-[THClient enableCredentialSharingModeForExtendedPANID:completion:];
-[THClient handleActiveNearbyNetworksResponse:error:isInternal:completion:];
-[THClient retrieveActiveCredentialsForNearbyNetworksWithCompletion:];
-[THClient getTheProxyWithPrefEntryCompletion:];
-[THClient threadSafePropertyQueue];
-[THClient getTheProxyWithErrorParameterCompletion:];
-[THClient retrieveCredentialsForBorderAgent:completion:];
-[THClient retrieveListOfPreferredNetworkEntriesInternally:ipV4NwSignature:ipv6NwSignature:wifiSSID:showCurrentEntry:completion:];
-[THClient retrievePreferredNetworkInternallyOnMdnsAndSig:];
-[THClient storeCredentialsForBorderAgentInternally:networkName:extendedPANId:activeOperationalDataSet:completion:];
-[THClient retrievePreferredCredentialsInternally:];
-[THClient ctcsDeletePreferredNetworkWithCompletion:];
```
