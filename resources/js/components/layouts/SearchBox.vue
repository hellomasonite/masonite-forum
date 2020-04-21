<template>
    <div class="row pb-5">
        <div class="col-md-4">
            <select class="custom-select" v-if="tags">
                <option selected>Open this select menu</option>
                <option v-bind:key="tag.id" v-for="tag in tags">{{ tag.name }}</option>
            </select>
        </div>
        <div class="col">
            <input type="text" class="form-control">
        </div>
    </div>
</template>

<script>
export default {
    data () {
        return {
            tags: []
        }
    },
    mounted() {
        axios.get('/api/tags/')
            .then(response => this.tags = response.data)
    }
}
</script>

<style>

</style>