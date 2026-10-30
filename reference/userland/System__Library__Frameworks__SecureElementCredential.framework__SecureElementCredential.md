# `/System/Library/Frameworks/SecureElementCredential.framework/SecureElementCredential`

iOS 27.2 dyld shared cache image. Version `71.9.3.0.0`. **[DSC]**

## Linked libraries (13)

- `/System/Library/PrivateFrameworks/SEService.framework/SEService`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`
- `/usr/lib/swift/libswiftCore.dylib`
- `/usr/lib/swift/libswiftCoreFoundation.dylib`
- `/usr/lib/swift/libswiftDispatch.dylib`
- `/usr/lib/swift/libswiftObjectiveC.dylib`
- `/usr/lib/swift/libswiftXPC.dylib`
- `/usr/lib/swift/libswift_Builtin_float.dylib`
- `/usr/lib/swift/libswift_Concurrency.dylib`
- `/usr/lib/swift/libswiftos.dylib`

## Objective-C: 3 classes, 5 protocols, 35 methods, 0 properties

### Class pages

Every class and protocol, with its methods: [`NSXPCProxyCreating`](../objc/NSXPCProxyCreating_SecureElementCredential.protocol.md), [`_TtC23SecureElementCredential17CredentialSession`](../objc/_TtC23SecureElementCredential17CredentialSession_SecureElementCredential.md), [`_TtC23SecureElementCredential9SECClient`](../objc/_TtC23SecureElementCredential9SECClient_SecureElementCredential.md), [`_TtCC23SecureElementCredential17CredentialSession26PresentmentIntentAssertion`](../objc/_TtCC23SecureElementCredential17CredentialSession26PresentmentIntentAssertion_SecureElementCredential.md), [`_TtP23SecureElementCredential18SECredentialServer_`](../objc/_TtP23SecureElementCredential18SECredentialServer__SecureElementCredential.protocol.md), [`_TtP23SecureElementCredential25SECredentialServerSession_`](../objc/_TtP23SecureElementCredential25SECredentialServerSession__SecureElementCredential.protocol.md), [`_TtP23SecureElementCredential27SECSessionCallbackInterface_`](../objc/_TtP23SecureElementCredential27SECSessionCallbackInterface__SecureElementCredential.protocol.md), [`_TtP23SecureElementCredential38SECredentialPresentmentIntentAssertion_`](../objc/_TtP23SecureElementCredential38SECredentialPresentmentIntentAssertion__SecureElementCredential.protocol.md)

### Classes

`_TtC23SecureElementCredential17CredentialSession`, `_TtC23SecureElementCredential9SECClient`, `_TtCC23SecureElementCredential17CredentialSession26PresentmentIntentAssertion`

### Protocols

`NSXPCProxyCreating`, `_TtP23SecureElementCredential18SECredentialServer_`, `_TtP23SecureElementCredential25SECredentialServerSession_`, `_TtP23SecureElementCredential27SECSessionCallbackInterface_`, `_TtP23SecureElementCredential38SECredentialPresentmentIntentAssertion_`

## Swift types (24)

`SecureElementCredential.CredentialSession`, `SecureElementCredential.CredentialSession.CardEmulationOptions`, `SecureElementCredential.CredentialSession.ConnectivityEvent`, `SecureElementCredential.CredentialSession.Credential`, `SecureElementCredential.CredentialSession.Credential.AccessLevel`, `SecureElementCredential.CredentialSession.Credential.InstanceInfo`, `SecureElementCredential.CredentialSession.Credential.InstanceInfo.InstanceType`, `SecureElementCredential.CredentialSession.Credential.State`, `SecureElementCredential.CredentialSession.ErrorCode`, `SecureElementCredential.CredentialSession.Event`, `SecureElementCredential.CredentialSession.NFCFieldInformation`, `SecureElementCredential.CredentialSession.PresentmentIntentAssertion`, `SecureElementCredential.CredentialSession.PresentmentIntentAssertion.State`, `SecureElementCredential.CredentialSession.SecureElementInfo`, `SecureElementCredential.CredentialSession.SecureElementInfo.CodingKeys`, `SecureElementCredential.CredentialSession.State`, `SecureElementCredential.PresentmentIntentAssertionDelegate`, `SecureElementCredential.SECClient`, `SecureElementCredential.SECPresentmentIntentAssertionState`, `SecureElementCredential.SECRemoteProxyObject`, `SecureElementCredential.SECSessionState`, `SecureElementCredential.SessionRemoteProxyObject`, `SecureElementCredential.XPCEventDelegate`, `conformance`

## Strings (69)

```
Throwing public error for internal error with description %{public}s
Internal assertion has been invalidated
Credential Session [%{public}s] acquired presentment intent assertion
SEC XPC: Already connected
[%{public}s]eventStreamContinuation init
Unknown error: %{public}s
SEC XPC: Starting new connection
Credential %{public}s hidden from public due to LOCKED state
No credential selected
[%{public}s] installationCompleted(%{public}s
Previously invalidated
Unable to start a new xpc connection
SEC XPC: Connection activated
Unknown internal credential state %{public}ld
No parent session
XPC error %s encountered
[%{public}s] rfFieldChanged(%{bool,public}d
[%{public}s] received HCI data)
Presentment Intent assertion for [%{public}s] has timed out
Credential in installed state without instance info
Acquiring assertion from invalid state is disallowed
[%{public}s] sessionEnded(%{public}@)
Yield event for cred: %{public}s
signalInvalidationOnEventStream
[%{public}s] invalidateEventStream(reason: %{public}s)
Starting credential session
XPC invalidated
Error %{public}s encountered when invalidating session
PresentmentIntentAssertion invalidated
Did not obtain presentment intent assertion
[self=%{public}s] eventStream init
[%{public}s] sessionErrorEvent(%{public}@
Successfully obtained presentment intent assertion
No valid credential selected
Credential Session [%{public}s] Start Success!
XPC interrupted
API call involved a credential that does not exist or the client does not have access to
User declined to grant permission for the operation
SecureElementCredential/CredentialSession+SecureElementCredential.swift
platformIdentifier
User not authorized to perform the operation
The user's iCloud account or passcode does not satisfy the conditions to use this service.
Internal error encountered
Network error. Please try again.
The Auth Sheet has been dismissed by the user and the underlying state has transitioned to management state
Client is not entitled to use this API
com.apple.seserviced
secureelementcredential
SecureElementCredential/CredentialSession.swift
Leaked credential!!!
API call to the session in a state that does not allow that function
The underlying shared resource has been relinquished and the session transitioned to Management state. Please try again.
Client is not in the foreground
The hardware storage has insufficient space for the provision attempt
Client requested the session to be invalidated
User auhthorization has timed out
Client attempted an unsupported SE command
Fatal error
com.apple.seserviced.credential.manager
One of the parameters is invalid
The current device and user configuration is ineligible for this service
The feature is unavailable
The presentment intent assertion has timed out.
API call involved an instance that does not exist in the target credential
API call involved a credential in a state that does not allow that function
hardwareReleaseVersionInfo
secureElementPlatformSigningCertificate
The product config ID is not valid
Requested resource is currently unavailable. Please try again.
```
