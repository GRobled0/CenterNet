// Auto-generated. Do not edit!

// (in-package semantic_SLAM.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class ObjectInfo {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.type = null;
      this.prob = null;
      this.tl_x = null;
      this.tl_y = null;
      this.width = null;
      this.height = null;
    }
    else {
      if (initObj.hasOwnProperty('type')) {
        this.type = initObj.type
      }
      else {
        this.type = '';
      }
      if (initObj.hasOwnProperty('prob')) {
        this.prob = initObj.prob
      }
      else {
        this.prob = 0.0;
      }
      if (initObj.hasOwnProperty('tl_x')) {
        this.tl_x = initObj.tl_x
      }
      else {
        this.tl_x = 0;
      }
      if (initObj.hasOwnProperty('tl_y')) {
        this.tl_y = initObj.tl_y
      }
      else {
        this.tl_y = 0;
      }
      if (initObj.hasOwnProperty('width')) {
        this.width = initObj.width
      }
      else {
        this.width = 0;
      }
      if (initObj.hasOwnProperty('height')) {
        this.height = initObj.height
      }
      else {
        this.height = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ObjectInfo
    // Serialize message field [type]
    bufferOffset = _serializer.string(obj.type, buffer, bufferOffset);
    // Serialize message field [prob]
    bufferOffset = _serializer.float32(obj.prob, buffer, bufferOffset);
    // Serialize message field [tl_x]
    bufferOffset = _serializer.int32(obj.tl_x, buffer, bufferOffset);
    // Serialize message field [tl_y]
    bufferOffset = _serializer.int32(obj.tl_y, buffer, bufferOffset);
    // Serialize message field [width]
    bufferOffset = _serializer.int32(obj.width, buffer, bufferOffset);
    // Serialize message field [height]
    bufferOffset = _serializer.int32(obj.height, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ObjectInfo
    let len;
    let data = new ObjectInfo(null);
    // Deserialize message field [type]
    data.type = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [prob]
    data.prob = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [tl_x]
    data.tl_x = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [tl_y]
    data.tl_y = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [width]
    data.width = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [height]
    data.height = _deserializer.int32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.type.length;
    return length + 24;
  }

  static datatype() {
    // Returns string type for a message object
    return 'semantic_SLAM/ObjectInfo';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '55a63526fe7c32ce41ef4e85ff85bb42';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string type
    float32 prob
    int32 tl_x
    int32 tl_y
    int32 width
    int32 height
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ObjectInfo(null);
    if (msg.type !== undefined) {
      resolved.type = msg.type;
    }
    else {
      resolved.type = ''
    }

    if (msg.prob !== undefined) {
      resolved.prob = msg.prob;
    }
    else {
      resolved.prob = 0.0
    }

    if (msg.tl_x !== undefined) {
      resolved.tl_x = msg.tl_x;
    }
    else {
      resolved.tl_x = 0
    }

    if (msg.tl_y !== undefined) {
      resolved.tl_y = msg.tl_y;
    }
    else {
      resolved.tl_y = 0
    }

    if (msg.width !== undefined) {
      resolved.width = msg.width;
    }
    else {
      resolved.width = 0
    }

    if (msg.height !== undefined) {
      resolved.height = msg.height;
    }
    else {
      resolved.height = 0
    }

    return resolved;
    }
};

module.exports = ObjectInfo;
