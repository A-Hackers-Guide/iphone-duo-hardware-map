# `RTBuddyKdebugEndpoint`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.RTBuddy`](../kexts/com.apple.driver.RTBuddy.md)
- Object size: `0x138` (312 bytes)
- Metaclass: `0xfffffe000ba23f20`; metaclass vtable `0xfffffe0008497ee8`; class vtable `0xfffffe0008497dc8`
- Registration (init): `0xfffffe000a940848`
- Superclasses: [`RTBuddyEndpoint`](RTBuddyEndpoint.md) → [`IOSlaveEndpoint`](IOSlaveEndpoint.md) → [`IOEventSource`](IOEventSource.md)

## Strings in its kext that name it (18)

- `IOReturn RTBuddyKdebugEndpoint::_kdebugSendFlushRequest()`
- `IOReturn RTBuddyKdebugEndpoint::_kdebugSendEnabledState()`
- `void RTBuddyKdebugEndpoint::_handleFlush(mbi_msg_t)`
- `void RTBuddyKdebugEndpoint::_handleHereIsMyBuffer(mbi_msg_t)`
- `RTBuddyKdebugEndpoint`
- `kIOReturnSuccess == _processor->getWorkLoop()->runAction(OSMemberFunctionCast(IOWorkLoop::Action, this, &RTBuddyKdebugEndpoint::_kdebugTypefilterChangedGated), this, arg)`
- `IOReturn RTBuddyKdebugEndpoint::_kdebugSendHostReadyAction()`
- `void RTBuddyKdebugEndpoint::_handleBufferRequest(mbi_msg_t)`
- `void RTBuddyKdebugEndpoint::_handleHereIsMyTypefilter(mbi_msg_t)`
- `kIOReturnSuccess == _processor->getWorkLoop()->runAction (OSMemberFunctionCast(IOWorkLoop::Action, this, &RTBuddyKdebugEndpoint::_kdebugSendEnabledState), this)`
- `kIOReturnSuccess == _processor->getWorkLoop()->runAction (OSMemberFunctionCast(IOWorkLoop::Action, this, &RTBuddyKdebugEndpoint::_kdebugSendHostReadyAction), this)`
- `site.RTBuddyKdebugEndpoint`
- `kIOReturnSuccess == _processor->getWorkLoop()->runAction (OSMemberFunctionCast (IOWorkLoop::Action, this, &RTBuddyKdebugEndpoint::_kdebugSendFlushRequest), this)`
- `IOReturn RTBuddyKdebugEndpoint::_kdebugSendTypefilterChangedNotification()`
- `void RTBuddyKdebugEndpoint::_messageHandler(void *, void *)`
- `RTBuddyKdebugEndpoint.cpp`
- `virtual void RTBuddyKdebugEndpoint::kdebugCallback(kd_callback_type, void *)`
- `virtual void RTBuddyKdebugEndpoint::enable()`
