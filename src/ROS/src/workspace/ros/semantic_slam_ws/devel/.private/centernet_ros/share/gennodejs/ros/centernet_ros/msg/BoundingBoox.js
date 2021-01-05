// Auto-generated. Do not edit!

// (in-package centernet_ros.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class BoundingBoox {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.Class = null;
      this.probability = null;
      this.xmin = null;
      this.ymin = null;
      this.xmax = null;
      this.ymax = null;
      this.depth = null;
    }
    else {
      if (initObj.hasOwnProperty('Class')) {
        this.Class = initObj.Class
      }
      else {
        this.Class = '';
      }
      if (initObj.hasOwnProperty('probability')) {
        this.probability = initObj.probability
      }
      else {
        this.probability = 0.0;
      }
      if (initObj.hasOwnProperty('xmin')) {
        this.xmin = initObj.xmin
      }
      else {
        this.xmin = 0;
      }
      if (initObj.hasOwnProperty('ymin')) {
        this.ymin = initObj.ymin
      }
      else {
        this.ymin = 0;
      }
      if (initObj.hasOwnProperty('xmax')) {
        this.xmax = initObj.xmax
      }
      else {
        this.xmax = 0;
      }
      if (initObj.hasOwnProperty('ymax')) {
        this.ymax = initObj.ymax
      }
      else {
        this.ymax = 0;
      }
      if (initObj.hasOwnProperty('depth')) {
        this.depth = initObj.depth
      }
      else {
        this.depth = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type BoundingBoox
    // Serialize message field [Class]
    bufferOffset = _serializer.string(obj.Class, buffer, bufferOffset);
    // Serialize message field [probability]
    bufferOffset = _serializer.float64(obj.probability, buffer, bufferOffset);
    // Serialize message field [xmin]
    bufferOffset = _serializer.int64(obj.xmin, buffer, bufferOffset);
    // Serialize message field [ymin]
    bufferOffset = _serializer.int64(obj.ymin, buffer, bufferOffset);
    // Serialize message field [xmax]
    bufferOffset = _serializer.int64(obj.xmax, buffer, bufferOffset);
    // Serialize message field [ymax]
    bufferOffset = _serializer.int64(obj.ymax, buffer, bufferOffset);
    // Serialize message field [depth]
    bufferOffset = _serializer.float64(obj.depth, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type BoundingBoox
    let len;
    let data = new BoundingBoox(null);
    // Deserialize message field [Class]
    data.Class = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [probability]
    data.probability = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [xmin]
    data.xmin = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [ymin]
    data.ymin = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [xmax]
    data.xmax = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [ymax]
    data.ymax = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [depth]
    data.depth = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.Class.length;
    return length + 52;
  }

  static datatype() {
    // Returns string type for a message object
    return 'centernet_ros/BoundingBoox';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '736162dbf88cd926f35ced1ad47b7fa7';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string Class
    float64 probability
    int64 xmin
    int64 ymin
    int64 xmax
    int64 ymax
    float64 depth
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new BoundingBoox(null);
    if (msg.Class !== undefined) {
      resolved.Class = msg.Class;
    }
    else {
      resolved.Class = ''
    }

    if (msg.probability !== undefined) {
      resolved.probability = msg.probability;
    }
    else {
      resolved.probability = 0.0
    }

    if (msg.xmin !== undefined) {
      resolved.xmin = msg.xmin;
    }
    else {
      resolved.xmin = 0
    }

    if (msg.ymin !== undefined) {
      resolved.ymin = msg.ymin;
    }
    else {
      resolved.ymin = 0
    }

    if (msg.xmax !== undefined) {
      resolved.xmax = msg.xmax;
    }
    else {
      resolved.xmax = 0
    }

    if (msg.ymax !== undefined) {
      resolved.ymax = msg.ymax;
    }
    else {
      resolved.ymax = 0
    }

    if (msg.depth !== undefined) {
      resolved.depth = msg.depth;
    }
    else {
      resolved.depth = 0.0
    }

    return resolved;
    }
};

module.exports = BoundingBoox;
