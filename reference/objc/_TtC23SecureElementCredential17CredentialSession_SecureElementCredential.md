# `_TtC23SecureElementCredential17CredentialSession`

- Image: [`/System/Library/Frameworks/SecureElementCredential.framework/SecureElementCredential`](../userland/System__Library__Frameworks__SecureElementCredential.framework__SecureElementCredential.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_TtCs12_SwiftObject`
- Protocols: `_TtP23SecureElementCredential27SECSessionCallbackInterface_`
- 8 instance variables, 0 properties, 6 instance methods, 0 class methods

## Instance variables

```
Builtin.DefaultActorStorage $defaultActor;
SecureElementCredential.SECRemoteProxyObject remoteProxy;
Swift.AsyncStream.Continuation SecureElementCredential.CredentialSession.Event _$s_GSg -> currentEventStreamContinuation;
_$sScS -> SecureElementCredential.CredentialSession.Event ? currentEventStream;
_$sSccySb Swift.Error ? sessionStartedContinuation;
Swift.Bool sessionStarted;
Foundation.UUID sessionIdentifier;
SecureElementCredential.CredentialSession.PresentmentIntentAssertion ? currentAssertion;
```

## Instance methods

```
-[_TtC23SecureElementCredential17CredentialSession sessionEndedWithError:];
-[_TtC23SecureElementCredential17CredentialSession installationCompletedWithCredentials:completionHandler:];
-[_TtC23SecureElementCredential17CredentialSession presentmentAssertionTimeoutWithError:completionHandler:];
-[_TtC23SecureElementCredential17CredentialSession receivedHciDataWithData:appletIdentifier:completionHandler:];
-[_TtC23SecureElementCredential17CredentialSession rfFieldChanged:completionHandler:];
-[_TtC23SecureElementCredential17CredentialSession sessionErrorEventWithReason:completionHandler:];
```
