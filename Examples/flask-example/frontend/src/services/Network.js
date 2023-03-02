export default class Network {
    constructor(host = "127.0.0.1", port = "5000") {
        this.host = host
        this.port = port
    }

    getRows = async (id) => {
        const response = await fetch(`http://${this.host}:${this.port}/rows?id=${id}`)
        const data = await response.json()
        return data
    }
}