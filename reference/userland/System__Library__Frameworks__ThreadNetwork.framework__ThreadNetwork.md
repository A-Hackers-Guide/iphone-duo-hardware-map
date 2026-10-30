# `/System/Library/Frameworks/ThreadNetwork.framework/ThreadNetwork`

iOS 27.2 dyld shared cache image. Version `446.0.4.0.0`. **[DSC]**

## Linked libraries (8)

- `/usr/lib/libTelephonyUtilDynamic.dylib`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libc++.1.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`
- `/System/Library/Frameworks/Security.framework/Security`
- `/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics`

## Objective-C: 13 classes, 3 protocols, 255 methods, 62 properties

### Class pages

Every class and protocol, with its methods: [`CTCSXPCServiceProtocol`](../objc/CTCSXPCServiceProtocol_ThreadNetwork.protocol.md), [`NSCoding`](../objc/NSCoding_ThreadNetwork.protocol.md), [`NSSecureCoding`](../objc/NSSecureCoding_ThreadNetwork.protocol.md), [`THClient`](../objc/THClient_ThreadNetwork.md), [`THCredentials`](../objc/THCredentials_ThreadNetwork.md), [`THNetworkSignature`](../objc/THNetworkSignature_ThreadNetwork.md), [`THPreferredNetworkEntry`](../objc/THPreferredNetworkEntry_ThreadNetwork.md), [`THPreferredThreadNetwork`](../objc/THPreferredThreadNetwork_ThreadNetwork.md), [`THThreadNetwork`](../objc/THThreadNetwork_ThreadNetwork.md), [`THThreadNetworkBorderAgent`](../objc/THThreadNetworkBorderAgent_ThreadNetwork.md), [`THThreadNetworkCredentials`](../objc/THThreadNetworkCredentials_ThreadNetwork.md), [`THThreadNetworkCredentialsActiveDataSetRecord`](../objc/THThreadNetworkCredentialsActiveDataSetRecord_ThreadNetwork.md), [`THThreadNetworkCredentialsDataSet`](../objc/THThreadNetworkCredentialsDataSet_ThreadNetwork.md), [`THThreadNetworkCredentialsStoreRecord`](../objc/THThreadNetworkCredentialsStoreRecord_ThreadNetwork.md), [`XPCInterface`](../objc/XPCInterface_ThreadNetwork.md)

### Classes

`NSError`, `THClient`, `THCredentials`, `THNetworkSignature`, `THPreferredNetworkEntry`, `THPreferredThreadNetwork`, `THThreadNetwork`, `THThreadNetworkBorderAgent`, `THThreadNetworkCredentials`, `THThreadNetworkCredentialsActiveDataSetRecord`, `THThreadNetworkCredentialsDataSet`, `THThreadNetworkCredentialsStoreRecord`, `XPCInterface`

### Protocols

`CTCSXPCServiceProtocol`, `NSCoding`, `NSSecureCoding`

### Properties

```
@property (class, TB,R) supportsSecureCoding;
@property (T@"NSXPCConnection",&,N,V_xpcConnection) xpcConnection;
@property (T^{dispatch_queue_s=},N,V_threadSafePropertyQueue) threadSafePropertyQueue;
@property (T^{dispatch_queue_s=},V_apiCAQueue) apiCAQueue;
@property (T@"NSString",&,V_mAppTeamID) mAppTeamID;
@property (T@"NSString",&,V_mAppName) mAppName;
@property (T@"NSString",&,V_mAppBundleID) mAppBundleID;
@property (T@"NSString",R,N,V_networkName) networkName;
@property (T@"NSData",R,N,V_extendedPANID) extendedPANID;
@property (T@"NSData",R,N,V_borderAgentID) borderAgentID;
@property (T@"NSData",R,N,V_activeOperationalDataSet) activeOperationalDataSet;
@property (T@"NSData",R,N,V_networkKey) networkKey;
@property (T@"NSData",R,N,V_PSKC) PSKC;
@property (TC,N,V_channel) channel;
@property (T@"NSData",R,N,V_panID) panID;
@property (T@"NSDate",R,N,V_creationDate) creationDate;
@property (T@"NSDate",R,N,V_lastModificationDate) lastModificationDate;
@property (T@"NSData",R,N,V_ipv4NwSignature) ipv4NwSignature;
@property (T@"NSData",R,N,V_ipv6NwSignature) ipv6NwSignature;
@property (T@"NSString",R,N,V_wifiSSID) wifiSSID;
@property (T@"NSString",R,N,V_wifiPassword) wifiPassword;
@property (T@"NSString",R,N,V_networkName) networkName;
@property (T@"NSData",R,N,V_extendedPANID) extendedPANID;
@property (T@"NSData",R,N,V_ipv4Signature) ipv4Signature;
@property (T@"NSData",R,N,V_ipv6Signature) ipv6Signature;
@property (T@"NSString",R,N,V_wifiSSID) wifiSSID;
@property (T@"THCredentials",R,N,V_credentialsRecord) credentialsRecord;
@property (T@"NSDate",R,N,V_creationDate) creationDate;
@property (T@"NSDate",R,N,V_lastModificationDate) lastModificationDate;
@property (T@"THThreadNetwork",R,N,V_network) network;
@property (T@"THNetworkSignature",R,N,V_networkSignature) networkSignature;
@property (T@"THThreadNetworkCredentialsActiveDataSetRecord",R,N,V_credentialsDataSetRecord) credentialsDataSetRecord;
@property (T@"NSString",C,N,V_userInfo) userInfo;
@property (T@"NSDate",R,N,V_creationDate) creationDate;
@property (T@"NSDate",R,N,V_lastModificationDate) lastModificationDate;
@property (T@"NSString",R,N,V_networkName) networkName;
@property (T@"NSData",R,N,V_extendedPANID) extendedPANID;
@property (T@"NSData",R,N,V_discriminatorId) discriminatorId;
@property (T@"NSData",C,N,V_masterKey) masterKey;
@property (T@"NSString",C,N,V_passPhrase) passPhrase;
@property (T@"NSData",C,N,V_PSKc) PSKc;
@property (TC,N,V_channel) channel;
@property (T@"NSData",C,N,V_PANID) PANID;
@property (T@"NSString",C,N,V_userInfo) userInfo;
@property (T@"THThreadNetworkCredentialsDataSet",&,N,V_credentialsDataSet) credentialsDataSet;
@property (TB,N,V_isActiveDevice) isActiveDevice;
@property (T@"THThreadNetworkBorderAgent",R,N,V_borderAgent) borderAgent;
@property (T@"THThreadNetworkCredentialsDataSet",R,N,V_credentialsDataSet) credentialsDataSet;
@property (T@"THThreadNetwork",R,N,V_network) network;
@property (T@"THThreadNetworkCredentials",&,N,V_credentials) credentials;
@property (T@"NSUUID",R,N,V_uniqueIdentifier) uniqueIdentifier;
@property (T@"NSString",R,N,V_keychainAccessGroup) keychainAccessGroup;
@property (T@"NSDate",R,N,V_creationDate) creationDate;
@property (T@"NSDate",R,N,V_lastModificationDate) lastModificationDate;
@property (T@"NSData",C,N,V_dataSetArray) dataSetArray;
@property (T@"NSString",C,N,V_userInfo) userInfo;
@property (T@"THThreadNetwork",R,N,V_network) network;
@property (T@"THThreadNetworkCredentials",R,N,V_credentials) credentials;
@property (T@"NSUUID",R,N,V_uniqueIdentifier) uniqueIdentifier;
@property (T@"NSString",R,N,V_keychainAccessGroup) keychainAccessGroup;
@property (T@"NSDate",R,N,V_creationDate) creationDate;
@property (T@"NSDate",R,N,V_lastModificationDate) lastModificationDate;
```

## Strings (213)

```
ds
ipv6
-[THClient init]
NA
-[THClient getTheProxyWithSetOfTHCredsParameterCompletion:]_block_invoke
v24@?0@\"NSUUID\"8@\"NSError\"16
-[THClient updatePreferredCredentialsInternally:]
Invalid input parameter: extendedPANID is required
grp
-[THClient getTheProxyWithPrefEntryCompletion:]_block_invoke
CFBundleName
app_name
v24@?0@8@\"NSError\"16
v24@?0@\"THThreadNetworkCredentialsActiveDataSetRecord\"8@\"NSError\"16
-[THClient ctcsRetrievePreferredNetworkInternallyWithCompletion:]
-[THClient countPreferredFrozenRecordsWithCompletion:]_block_invoke_2
credentials
-[THClient getTheProxyWithRecordCompletion:]_block_invoke
-[THClient connectToXPCService]
NO
-[THClient getConnectionEntitlementValidity:]_block_invoke
-[THClient retrieveCredentialsForExtendedPANID:completion:]_block_invoke
-[THClient enableCredentialSharingModeForExtendedPANID:completion:]
-[THClient getTheProxyWithBoolCompletion:]_block_invoke
ssid
-[THClient startThreadBRScanInternally:]
-[THClient retrieveCredentialsForBorderAgent:completion:]_block_invoke
ch
panid
wifissid
__teamid_local__
pp
cred
.dev
com.apple.Flagstone.flagstoneTHClientAPIInfo
-[THClient checkPreferredNetworkForActiveOperationalDataset:completion:]_block_invoke
-[THClient getTheProxyWithTHCredsAndUuidParametersCompletion:]_block_invoke
-[THClient getTheProxyWithResultBlockCompletion:]_block_invoke
api_enum
false
-[THClient ctcsCleanPreferredAndFrozenThreadNetworksWithCompletion:]
-[THClient countNonAppleRecordsWithCompletion:]_block_invoke_2
com.apple.ThreadNetwork.xpc
thclient
-[THClient dealloc]
true
-[THClient ctcsRetrieveOrGeneratePreferredNetworkInternallyWithCompletion:]
-[THClient retrieveCredentialsForBorderAgent:completion:]
-[THClient getTheProxyWithNwSignatureCompletion:]_block_invoke
uuid
api_return_error_message
Failed to retrieve record
v24@?0Q8@\"NSError\"16
-[THClient ctcsAddPreferredNetworkWithCompletionInternally:extendedPANId:borderAgentID:ipV4NwSignature:ipv6NwSignature:wifiSSID:wifiPassword:completion:]
-[THClient isPreferredNetworkAvailableWithCompletion:]
-[THClient isPreferredNetworkAvailableWithCompletion:]_block_invoke
v24@?0@\"NSSet\"8@\"NSError\"16
ipv4
v20@?0B8@\"NSError\"12
-[THClient ctcsAddPreferredNetworkWithCompletionInternally:extendedPANId:borderAgentID:ipV4NwSignature:ipv6NwSignature:wifiSSID:wifiPassword:completion:]_block_invoke
-[THClient ctcsDeletePreferredNetworkForNetworkSignatureInternallyWithCompletion:extendedPANId:ipV4NwSignature:ipv6NwSignature:wifiSSID:completion:]_block_invoke
unspecified
net
cr
name
com.apple.ThreadNetwork
Invalid input parameter caused error
mk
-[THThreadNetworkCredentialsStoreRecord initWithCoder:]
.
-[THClient ctcsDeletePreferredNetworkWithCompletion:]
-[THClient retrievePreferredCredentials:]
.staging
Failed to retrieve Preferred Network Entry
-[THClient retrieveNetworkSignatureWithCompletion:]
-[THClient checkPreferredNetworkForActiveOperationalDataset:completion:]
CTCS XPC Client Thread Safe Property Queue (RCP Dataset)
.debug.
-[THClient validateAODInternally:completion:]
-[THClient retrieveCredentialsForUUID:completion:]
.beta.
-[THClient ctcsDeleteActiveDataSetRecordWithUniqueIdentifier:completion:]
Invalid input parameter
v24@?0@\"NSArray\"8@\"NSError\"16
-[THClient retrievePreferredNetworkWithNoScan:]
passwd
creds
CTCS XPC Client Thread Safe Property Queue
-[THClient retrieveListOfPreferredNetworkEntriesInternally:ipV4NwSignature:ipv6NwSignature:wifiSSID:showCurrentEntry:completion:]
-[THClient rapportSendForPreferredNetworkWithMessage:completion:]
-[THClient countNonAppleRecordsWithCompletion:]
active
@\"NSMutableDictionary\"8@?0
-[THClient ctcsStoreThreadNetworkCredentialActiveDataSetInternally:network:credentialsDataSet:waitForSync:completion:]
-[THClient initWithKeychainAccessGroup:]
.staging.
app_teamID
api_is_internal
-[THClient countPreferredFrozenRecordsWithCompletion:]
-[THClient storeCredentialsForBorderAgent:activeOperationalDataSet:completion:]_block_invoke
-[THClient retrieveOrGeneratePreferredNetworkInternally:]
info
-[THClient connectToXPCService]_block_invoke
ThreadCredentialsStore
v12@?0B8
-[THClient retrieveActiveDataSetRecordInternallyForExtendedPANID:completion:]
Success
ui
ba
-[THClient getTheProxyWithTHCredsParameterCompletion:]_block_invoke
.dev.
app_bundleID
XPC method request timed out after %@ seconds
-[THClient enableCredentialSharingModeInternallyForExtendedPANID:completion:]
sig
.beta
probe
api_return_error_code
-[THClient retrievePreferredCredentialsInternally:]
nk
-[THClient ctcsCleanKeychainThreadNetworksWithCompletion:]
-[THClient retrieveNetworkSignatureWithCompletion:]_block_invoke
-[THClient retrieveCredentialsForExtendedPANID:completion:]
v8@?0
-[THClient getTheProxyWithNwSignatureCompletion:]
-[THClient getConnectionEntitlementValidity]_block_invoke
v40@?0@\"NSData\"8@\"NSData\"16@\"NSString\"24@\"NSError\"32
-[THClient startThreadBRScanInternally:]_block_invoke_2
v16@?0@\"NSError\"8
-[THClient getTheProxyWithErrorParameterCompletion:]_block_invoke
psk
xp
-[THThreadNetworkCredentialsActiveDataSetRecord initWithCoder:]
THClient.CAapi.queue
api_is_success
CTCS Client XPC Connection Queue
-[THClient ctcsRetrieveActiveDataSetRecordWithUniqueIdentifier:completion:]
-[THClient enableCredentialSharingModeInternallyForExtendedPANID:completion:]_block_invoke
-[THClient rapportBrowseForPreferredNetworkWithCompletion:]
-[THClient rapportConnectForPreferredNetworkWithCompletion:]
-[THClient retrieveAllCredentials:]
-[THClient retrieveAllActiveCredentials:]
[accessGroup] Keychain error %d
YES
-[THClient deleteCredentialsForBorderAgent:completion:]
-[THClient storeCachedAODasPreferredNetwork:completion:]_block_invoke
Failed to retrieve nearby active record
-[THClient enableCredentialSharingModeForExtendedPANID:completion:]_block_invoke
thserver
.debug
lm
dscreds
api_current_environment
-[THClient retrievePreferredNetworkInternallyOnMdnsAndSig:]
Client: %s:%d - Enabling Credential Sharing Mode
Client: %s:%d - Counting 3P saved Border Agent credentials
%s:%d: - Error: %@
%s:%d: - Response: isPreferred : %d
Client: %s - Retrieve Network Signature proxy check
Client: %s:%d - BR scan completed with %lu names, error: %@
Rapport: Client: %s:%d - Initiating Rapport Browse for Credential Share
Rapport: Client: %s:%d - Initiating Rapport Connect for Credential Share
%s:%d: - Response: recordUniqueIdentifier %@ error %@
%s:%d: - Completion with error : %@
%s:%d: - Response: isPreferredAvailable : %d
CAInitDispatchQueue failed to initialize
Could not retrieve bundle ID, returning Unknown environment
Client: %s Failed to retrun record, error: %@ \n
%s:Client:thread safe property queue - deallocated...
Client: %s:%d - Calling Server remoteObjectProxyWithErrorHandler
Client: %s Returning record successfully, error: %@ \n
Client: %s - Error: %@
Client: %s:%d - Counting frozen preferred network records
Client: %s - CTCS XPC Client is interrupted.
Client: %s - CTCS XPC Client is invalidated.
CAInitDispatchQueue initialized successfully, getAppName: %@, AppTeamID: %@, AppBundleID: %@
Handle invalidated XPC Connection
clientProxyWithErrorHandler connected=%@
XPC Client - isConnected: %@
Client: %s - clientProxyWithErrorHandler Error: %@
Successfully established connection
Client:apiCAQueue not initialized,skipping analytics
Client: %s - XPC Client Init done
Client: %s:%d - Proxy Call Back with error %@
%s:Client:THClient.CAapi.queue - deallocated...
synchronousRemoteObjectProxy - %@
Client: %s:%d - Starting Thread BR mDNS scan
Rapport: Client: %s:%d - Initiating Rapport Send for Preferred Network with message
%s:%d: - Response: %@
getAppTeamID return null,as accessGroup is null
Failed to get main bundle
Client:Couldn't get flagstoneTHClientAPIInfo, as apiCAQueue queue object not initialized
XPC Client - set connected: %@
Client: %s:%d - Retrieve Network Signature calling server proxy API
Handle interrupted XPC Connection
%s:%d: Could not decode uniqueIdentifier
Client: %s - connectToXPCService Connection resumed
Failed to create synchronous remote object proxy: %@
%s:%d: - Response: count = %lu, error = %@
Client: %s:%d
Connection failed while trying to get async remote object proxy (%@)\n
Client: %s:%d - Read list of Preferred Network Entries
accessGroup:%@
Invalidating XPC connection.
clientProxyWithErrorHandler: %@
synchronousRemoteObjectProxyWithErrorHandler: %@
%@
Client: %s - XPC Client Init Failed
%s:Client:Connection - deallocated...
Failed to ping service.
Client:Triggered com.apple.Flagstone.flagstoneTHClientAPIInfo
Client: %s:%d - Credential Sharing Mode error: %@
getAppName return null
```
